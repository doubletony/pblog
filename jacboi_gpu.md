Title: Jacobi iteration on GPU
Author: doubletony
Date: 11 July 2012

## Source Code

Here it is. \[[download](https://dl.dropbox.com/u/3461566/jacobi.cu )\]

## Warm Tip

The following code has potential problem. See an related [post](./doodle0017.html ).


<a name="overview"> </a>
## Overview

     while ( err > ERROR_TOL) // do the iteration untill err is less than tolerance
     {
          // 1. Copy X to x_old
          for (int i =0; i < dim; i++)
          {
               x_old[i] = X[i];
          }
          // 2. Compute X by A x_old
          
          cudaMemcpy( X_old_d, x_old, sizeof(float) * dim, cudaMemcpyHostToDevice);
          matMultVec<<<dimB, dimT>>>(LU_d, X_old_d, tmp, dim, dim); // use x_old to compute LU X_old and store the result in tmp
          substract<<<dimB, dimT>>>(B_d, tmp, X_d, dim);        // get the (B - LU X_old), which is stored in X_d
          diaMultVec<<<dimB, dimT>>>(diag_d, X_d, dim);         // get the new X
           
          // 3. copy the new X back to the Host Memory
          cudaMemcpy( X, X_d, sizeof(float) * dim, cudaMemcpyDeviceToHost);

          // 4. calculate the norm of X_new - X_old
          substract<<<dimB, dimT>>>(X_old_d, X_d, tmp, dim);
          VecAbs<<<dimB, dimT>>>(tmp, dim);
          VecMax<<<dimB, dimT>>>(tmp, dim);
          
          // copy the max value from Device to Host

          cudaMemcpy( max, tmp, sizeof(float), cudaMemcpyDeviceToHost);
          err = (*max);
     }
 
<a name="multiply"> </a>
## Matrix multiply vector

    
    __global__ void matMultVec( float * mat_A, 
                                float * vec, 
                                float * rst, 
                                int dim_row, 
                                int dim_col)
    {
         int rowIdx = threadIdx.x + blockIdx.x * blockDim.x; // Get the row Index 
         int aIdx;
         while( rowIdx < dim_row)
         {
              rst[rowIdx] = 0; // clean the value at first
              for (int i = 0; i < dim_col; i++)
              {
                   aIdx = rowIdx * dim_col + i; // Get the index for the element a_{rowIdx, i}
                   rst[rowIdx] += (mat_A[aIdx] * vec[i] ); // do the multiplication
              }
              rowIdx += gridDim.x * blockDim.x;
         }
         __syncthreads();
    }


<a name="add"> </a>
## Matrix addition/substraction 

     __global__ void substract(float *a_d, 
                               float *b_d, 
                               float *c_d, 
                               int dim)
     {
          int tid = threadIdx.x + blockIdx.x * blockDim.x;
          while ( tid < dim )
          {
               c_d[tid] = a_d[tid] - b_d[tid];
               tid += gridDim.x * blockDim.x;
          }
     }

<a name="norm"> </a>
## Vector Norm

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

