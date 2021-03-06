Title: Eigen: a brief intro 
Author: doubletony
Date: 25 July 2012

## Emm, what is Eigen?

Well, since you didn't skip this paragraph, it's necessary to introduce a bit what Eigen is. I quote what is showed on its [official website](http://eigen.tuxfamily.org/index.php?title=Main_Page ), 

> "Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms."

## Why use Eigen?

> "I need a sparse linear solver."

From my personal experience, one of my projects was using [TAUCS](http://www.tau.ac.il/~stoledo/taucs/ ), which has been unsupported for a very long time. It's not working quite well as long as the project getting larger. Finally, I decided to switch to something else which is a bit more modern.

Another thing made me happy is that Eigen is portable. There is no hassle to link a bunch of lib files (.lib or .a). Thus, it's fairly easy to use. Just download it, extract it, put it under my project directory and use it. No configuration, no building stuff.

## Now, show me some examples?

Okey-dokey, I'll show a piece of code while the [official document](http://eigen.tuxfamily.org/dox/ ) 
 of Eigen is also very helpful. Some code is able to be compiled on both Eigen 3.1.1 and Eigen 3.0. However, the program may have problems at running time. Hence, to save the trouble, I should declare that my code is working on Eigen 3.1.1, which is released on 22 July 2012. (Yeah, I like being up-to-date.) 

### Compute Singular values


    #include "Eigen/Dense"
    void SVD_eigen(double a[3][3], double sigma[3])
    {
         Eigen::Matrix3d A;
         for (int i = 0; i < 3; i++)
         {
              for (int j = 0; j < 3; j++)
              {
                   A(i,j) = a[i][j];
              } //end of j
         } //end of i

         Eigen::JacobiSVD<Eigen::Matrix3d> svd(A);
         Eigen::Vector3d sgm = svd.singularValues();

         for (int j = 0; j < 3; j++)
         {
              sigma[j] = sgm[j];
         }
    }


