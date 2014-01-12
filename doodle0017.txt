Title: Again, Jacobi iteration on GPU
Author: doubletony
Date: 15 August 2012

## What's updated?

Here is my old [post](./jacboi_gpu.html ). The purpose of that post is just to provide code snippets for my
[presentation](http://www.cse.msu.edu/~wangyua6/presentation/gpusolver.html ).
In that post, however, the code of VecNorm ( VecMax ) is not working correctly for some cases.

As always, here is the new code. \[[download](https://dl.dropbox.com/u/3461566/jacobi_new.cu )\]

## So, what's the problem?


    __global__ void VecMax( float * vec,  int dim)
    {
         int tid = threadIdx.x + blockIdx.x * blockDim.x;
         while (dim > 1)
         {
              int mid = dim / 2; // get the half size
              if ( tid < mid)    // filter the active thread
              {
                   if ( vec[tid] < vec[tid+mid] ) // get the larger one between vec[tid] and vec[tid+mid]
                        vec[tid] = vec[tid+mid];  // and store the larger one in vec[tid]
              }

              //deal with the odd case
              if ( dim % 2 )       // if dim is odd...we need care about the last element
              {
                   if ( tid == 0 ) // only use the vec[0] to compare with vec[dim-1]
                   {
                        if ( vec[tid] < vec[dim-1] )
                             vec[tid] = vec[dim-1];
                   }
              }

              __syncthreads(); // sync all threads
              dim /= 2;        // make the vector half size short.
         }
    }


This function may not work properly when the number of blocks is greater than 1. The reason is that
_syncthreads()_ only ** sync threads within one block  **. So, it'll cause the problem. For example,
if the dim = 1024 and the thread number is 256, thus the block number is 4. In the first block, thread 0 compares
vec[0] and vec[512]. Then it waits all other threads in the first block until they finish the job. Now, in the first block,
the new dim is 512, so thread 0 compares vec[0] and vec[256]. However, we don't know whether vec[256] is safe
to use or not, because the thread-0 in block 2 may still work on comparing vec[256] and vec[256+512] in its first iteration
of the second block. Thus, we have troubles.

## What's the new solution?

We have several options. Since [CUDA](http://developer.nvidia.com/cuda/cuda-downloads ) 4.0, [thrust](https://code.google.com/p/thrust/ ) has been included in the official package. So we can use a thrust function of vector maximum as an option. 

Also, we can solve the problem still with some basic CUDA codes. The strategy now is to use a loop on CPU and
let GPU does the job just for one iteration. The following code implements the idea of breaking the loop step by step.


    void VecMax( float * vec,  int dim, int dimB, int dimT)
    {

         while (dim > 1)
         {
              VecMaxOneStepCompare<<<dimB, dimT>>>(vec, dim);

              // if the dimension is odd.
              if( dim % 2)
              {
                   SwapForOddDim<<<1,1>>>(vec, dim);
              }
              dim /= 2;        // make the vector half size short.
         }

         // compare last two values
         SwapForOddDim<<<1,1>>>(vec, 2);
    }

And the VecMaxOneStepCompare is just a single step to compare the element with index $i$ and $i+\frac{dim}{2}$.


    __global__ void SwapForOddDim(float * vec, int dim)
    {
         if ( vec[0] < vec[dim-1] )
              vec[0] = vec[dim-1];
    }


    __global__ void VecMaxOneStepCompare( float * vec,  int dim)
    {
         int tid = threadIdx.x + blockIdx.x * blockDim.x;
         int mid = dim / 2; // get the half size

         while( tid < mid)
         {
              if ( tid < mid)    // filter the active thread
              {
                   if ( vec[tid] < vec[tid+mid] ) // get the larger one between vec[tid] and vec[tid+mid]
                        vec[tid] = vec[tid+mid];  // and store the larger one in vec[tid]
              }

              tid += gridDim.x * blockDim.x;
         }
         __syncthreads();
    }






