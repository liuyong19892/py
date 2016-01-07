for x in xrange(1,10):
	print x

for chx in 'ABC':
	print chx

from collections import Iterable
bool = isinstance('abc', Iterable)
print bool

for i, value in enumerate(['A', 'B', 'C']):
	print i, value

for x, y in [(1,2), (2,4), (3,9)]:
	print x, y

d = {'a':1, 'b':2, 'c':3}
for k in d.keys():
	print k
for v in d.values():
	print v
for k,v in d.items():
	print k, v