Title: Last non-zero digit of a factorial
Author: doubletony
Date:  5 August 2012

## What's the problem?

Given a number $ n $, find the last non-zero digit of $ n! $. For example, given 5, the
last non-zero digit is 2. (since $ 5! = 120 $.)

## Emm, brute-force first.

Well, it seems not an easy problem. The factorial increases fast, so the brute-force method 
as following will explode very fast. It's overflow when n is only as small as 20.
        
    int bruteLastNonzerodigit(int n)
    {
         int factorial = 1;

         for (int i = 1; i <= n; i++)
         {
              factorial *= i;
         }

         while( (factorial % 10) == 0 )
         {
              factorial /= 10;
         }
         return factorial % 10;
    }

## A better one.

So, if we think a bit deeply, we'll find that we are not necessary to store the entire result of a factorial.
What if we can store a portion of the several digits from last non-zero digit? And take care the multipler of 5
since zero of a factorial is produced by the factor of 5. For example, $5! = \cdots 0$, $10! = \cdots 00$. 
Thus, we only need to keep a small portion
of last non-zero digits. 

    int getFiveOrder(int &n)
    {
         // we need change n
         int count = 0;
         while ( (n % 5) == 0  )
         {
              count += 1;
              n /= 5;
         }
         return count;
    }

    int lastNonzeroDigit(int n)
    {
         int lastPortion = 1;

         for( int i = 1; i <= n; i++ )
         {
              int remain = i;
              int fiveOrder = getFiveOrder(remain);
              int divider = 1<<fiveOrder;
              lastPortion /= divider;
              lastPortion *= remain;
              if (lastPortion < 0)
              {
                   cout<<"Warnning: overflow..\n";
              }
              lastPortion = lastPortion % 10000000;
         }

         return lastPortion % 10;
    }


It's a little better than the brute-force version. However, it's still exploded around 250.
The reason is not difficult to find: we can only keep a very limited last portion (% 10000000).
And it's still a waste.

## Now, any better one?

So, is there any better one? Yes. If we are given a number of the format $ n = a \cdot b \cdot c $,
the last digit also can be computed as ( ((a % 10) * (b % 10) * (c % 10)) % 10). So can we borrow the
same idea to compute the last non-zero digit. For instance, if we have a function $ f $, where $f(n)$
will give us the last non-zero digit of $ n $, then can we compute $ f(abc)= f( f(a) f(b) f(c) ) $?

Unfortunately, the answer is no. For example $n = 12 \cdot 5$, $f(12 \cdot 5) = 6$, while $f(f(12)f(5))=1$.
Let's take a look why it's not working as we expected. The reason is that we have a pair of $2$ and $5$, which
will create a $0$ at the end. Thus, if we can get rid of the pairs of $2$ and $5$ from $n$, then we should be safe to compute
last digit similar as the above strategy. Thus, we have the following program, which works better. 


    int getOrder(int &n, int d)
    {
         int count = 0;
         while ( (n % d) == 0  )
         {
              count += 1;
              n /= d;
         }
         return count;
    }

    int lastNonzeroDigit(int n)
    {
         int twoOrderCount = 0; // we only need count the order of 2, think it why?
         int lastDigit = 1;

         for( int i = 1; i <= n; i++ )
         {
              int remain = i;
              int fiveOrder = getOrder(remain, 5);
              int twoOrder = getOrder(remain, 2);
              twoOrderCount += (twoOrder - fiveOrder);
              lastDigit = (lastDigit * remain % 10);
         }

         for (int i = 0; i < twoOrderCount; i++)
         {
              lastDigit = ( lastDigit * 2 ) % 10;
         }
         return lastDigit;
    }

This piece of code works nice for the input n as large as 10000000 within a blink. 
However, the story is not end. It takes a while on my computer to get the result of 100000000.
Can we improve it from the aspect of time-complexity? The answer is _YES_ but there is not enough
space in the margin to write it :) 
