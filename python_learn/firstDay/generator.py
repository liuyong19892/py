#-coding:utf-8

#List Comprehension
L = [x*x for x in range(10)]
print L

#Gnerator
g = (x*x for x in range(10))
print g
print next(g)

def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 2
	print 'step 3'
	yield 3
o = odd()
next(o)
next(o)
