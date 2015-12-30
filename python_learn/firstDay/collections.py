#coding:utf-8

#List有序的集合， 可以随时添加删除
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)

classmates.append('Jay')
classmates.insert(1, 'Jack')
print classmates

classmates.pop();
classmates.pop(1)
print classmates

classmates[1] = 'Jay'
print classmates

p = ['asp', 'jsp']
s = ['java', 'python', p, 'c']
print s
print s[2][1]

#Tuple 和List类似 但是初始化后就不能修改
classmate = ('Michael', 'Bob', 'Tracy')
#定义一个元素的tuple
t = (1,)
print t

#Dict 键值存储， 有极快的查找速度。但是占用空间大.key必须为不可变对象
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print d['Michael']

#set 数学意义上无序无重复元素的集合
s = set([1,2,3])
print s

s2 = set([2,3,4])
print s & s2
print s | s2

#s3 = set([[1,2,3],2,3]) --unhashable type: 'list'
#print s3








