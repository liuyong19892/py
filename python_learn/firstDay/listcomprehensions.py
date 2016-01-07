#-coding:utf-8
print list(range(1, 11))

L = []
for x in xrange(1,11):
	L.append(x*x)
print L

#列表生成式
print [x*x for x in xrange(1, 11)]
print [x*x for x in xrange(1, 11) if x%2 == 0]

#两层循环
print [x+y for x in ['a','b','c'] for y in '123']

#列出当前目录所有文件及文件名
import os 
print [d for d in os.listdir('.')]

L = ['HELLO', 'WORLD',18, 'apple' , None]
print [s.lower() for s in L if isinstance(s, str)]
