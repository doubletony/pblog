Title: [Code] Count the number of inversions
Author: doubletony
Date: 17 March 2013

## Problem Statement 

Given an unsorted array of distinct integers, find the number of inversions. (Check the full definition [here](http://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)) For example, given "3 1 2 5 4", we have three inversions "3 1", "3 2" and "5 4".

## Famous Solution

We know that the brute-force way has the time complexity of $O(n^2)$, where $n$ is the number of integers. Well, the famous optimal solution based on divide-and-conquer is $O(nlog(n))$. However, I'm going to show my thoughts. 

**Update**: Unfortunately, after finishing this post, I found a much more compressive article about this problem. -_-|| Check it [here](http://www.yeminghu.com/?p=34).

## Looks-so-nice one

This solution looks so nice at first glance. Unfortunately, it works as bad as the brute-force. However, the idea is worth to be known. First observation is that if we know the index of the minimum integer, than we know how many inversions are related to it. Yes, the number is exactly the index. (Well, computer guys should be comfortable with 0-index array.) Now, if we remove this minimum, and repeat this step. We should be able to get the total number of inversions. It doesn't look nice at all. Why? It's still $O(n^2)$. To an experienced programmer, there is a scent of using a min-heap somehow to make the average time of finding minimum element $O(log(n))$. 

## Realistic one

The second method is not related to the above one at all. It's based on an auxiliary binary search tree. The tree node will store necessary information to compute the inversion number. When inserting an new node into a BST, if we can easily know how many nodes are greater than this one, then we know the number of inversions caused by this node. It's not hard to do. For each node, we only need to store the number of nodes in it right subtree plus itself.

    class TreeNodeInverse
    {
    
    public:
        TreeNodeInverse * left;
        TreeNodeInverse * right;
        int key;
        int counter;
        
        TreeNodeInverse(int k)
        {
            key = k;
            counter = 1;
            left = right = NULL;
        }
    
    };

Now, we gradually insert each integer in its original order. When inserting a integer, we count the number of inversions along the traversing path.

    int getNumOfInversion( vector<int> nums )
    {
        TreeNodeInverse * root = new TreeNodeInverse(nums[0]);
        int counter = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            int invCounter = 0;
            InsertBSTInverse(root, nums[i], invCounter);
            counter += invCounter;
        }
        return counter;
    }

The crucial thing here is how to do the insertion and counting? Actually, it's not that complicated. When traversing along a node's right child, we increase this node's counter by 1 since the new node will belong to its right subtree; when traversing along a node's left child, we increase the inversion counter by this node's counter of right children.

    void InsertBSTInverse(TreeNodeInverse * root, int key, int &counter)
    {
        if ( root->key > key)
        {
            // go left
            counter += root->counter;
            if ( root->left != NULL )
            {
                InsertBSTInverse(root->left, key, counter);
            }
            else
            {
                TreeNodeInverse * node = new TreeNodeInverse(key);
                root->left = node;
            }
        }
        else
        {
            // go right
            root->counter++;
            if ( root->right != NULL )
            {
                InsertBSTInverse(root->right, key, counter);
            }
            else
            {
                TreeNodeInverse * node = new TreeNodeInverse(key);
                root->right = node;
            }
        }
               
    }

Done!

## Comments

Obviously, there are issues of this algorithm making it not optimal. First, the worst case is $O(n^2)$ when the input will generate a not well-balanced tree. Second, it's definitely a serial algorithm. So, we will lose the performance improvement from parellization. 
