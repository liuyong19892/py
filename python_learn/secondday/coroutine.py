#-coding:utf-8

#协程：子程序调用总是一个入口，一次返回。协程看上去也是
#   子程序，但是执行过程中，在子程序内部可中断，然后转而执行别的子程序，
#   在适当的时候再返回来接着执行。

def consumer():
	r = ''
	while True:
		n = yield r
		if not n :
			return
		print '[CONSUMER] Consuming %s....'% n
		r = '200 ok'

def produce(c):
	c.send(None)
	n = 0
	while n<5:
		n = n + 1
		print '[PRODUCER] producing %s...' % n
		r = c.send(n)
		print '[PRODUCER] Consumer return %s...' % r
	c.close()

c = consumer()
produce(c)