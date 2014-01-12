Title: [IMO 2012] Problem 2
Author: doubletony
Date:  7 August 2012

## Problem

Let $ n \geq 3 $ be an integer, and let $ a\_2, a\_3, \cdots , a\_n$ be positive real numbers such that
$ a\_2 a\_3 \cdots a\_n = 1 $. Prove that

$$ (1+a\_2)^2 (1+a\_3)^3 \cdots (1+a\_n)^n > n^n  $$


## Hint: arithmetic mean $\geq$ geometric mean

For each term, $(1+a\_k)^k$, we may try to make it looks like something of arithmetic mean. So, he have

$$ ((k - 1) (\frac{1}{k-1}) + a\_k)^k $$

Now we have,

$$ ((k - 1) (\frac{1}{k-1}) + a\_k)^k  \geq k^k a\_k (\frac{1}{k - 1})^{k-1} $$

which means $ (1+a\_k)^k \geq a\_k\frac{k^k}{{(k-1)}^{k-1}} $

Now, what follows is straightforward.


