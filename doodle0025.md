Title: Python Poem
Author: doubletony
Date: 13 January 2014


## [255B](http://codeforces.com/problemset/problem/255/B)

	z='yx'
	y,x=map(raw_input().count,z)
	print abs(y-x)*z[x>y]


## [384A](http://codeforces.com/problemset/problem/384/A)

    n = int(raw_input())
	print (n*n+1)/2
	al = lambda x: "C."[x%2]
	alr = ["".join(map(al, range(n))), "".join(map(al, range(1,n+1)))]

	def pr(x):
		print alr[x%2]

	map(pr, range(n))
