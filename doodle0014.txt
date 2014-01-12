Title: [IMO 2012] Problem 4
Author: doubletony
Date:  8 August 2012

## Problem

Find all functions $ f: \mathbb{Z} \to \mathbb{Z} $ such that, for all integers $a,b,c$ that
satisfy $a+b+c=0$, the following equality holds:

$$ {f(a)}^2 + {f(b)}^2 + {f(c)}^2 = 2{f(a)}{f(b)} + 2{f(b)}{f(c)} + 2{f(c)}{f(a)} $$


## Some simple results

First, let $a=b=c=0$ and we will have  $f(0)=0$. 

Second, Set $c=0$ and $b=-a$, we get $f(a)=f(-a)$ (wow,it's an even function).

Then, if we replace $c$ by $a+b$ (since $f(c)=f(-a-b)=f(a+b)$), we can obtain the following equality:

$$ {(f(a+b) - (f(a)+f(b))) }^2 = 4f(a)f(b) $$


## Find the recurrence relation

Now, we have enough knowledge to analyze the properties of function $f$. 

_First_, we have $f(z) \geq 0$  for all $z \in \mathbb{z}$ or  $f(z) \leq 0$  for all $z \in \mathbb{z}$
It's not difficult to see since if we can find two values $z\_1, z\_2$ having opposite signs, then 
$4f(z\_1)f(z\_2) < 0$ which is impossible.

_Second_, if we have a non-negative function $f$ as a solution, then $g(z)=-f(z)$ is also a solution.
It's still not difficult to see since each term in the original equality is of order two.

If we assume $f$ is a non-negative solution, we can take out the square safely to obtain the following equality:

$$ f(a+b) - (f(a)+f(b)) = \pm 2\sqrt{f(a)f(b)} $$

which also means

$$ f(a+b) = (\sqrt{f(a)} \pm \sqrt{f(b)})^2$$

Replace $b$ by $1$, we can get the recurrence relation:

$$ f(a+1) = (\sqrt{f(a)} \pm \sqrt{f(1)})^2$$

To make it simple, we can replace function $f$ by a function $g$, where $f(a) = g^2(a), g(a) \geq 0$. (Think: why can we do this?)

Now, the equality will look like $ g^2(a+1) = ( g(a) \pm g(1) )^2 $, which means

$$ g(a+1) = \pm (g(a) \pm g(1) )  $$

## All solutions?

Well, I will leave it there. (HINT: there are two classes of non-trivial solutions.)

