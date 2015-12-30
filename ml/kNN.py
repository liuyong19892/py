from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def remove_blank(e):
	return e.replace('\n', '')

if __name__  == '__main__':
	

	group = []
	labels = []
	with open('txt/kNN.txt', 'r') as f:
		for line in f.readlines():
			arr = line.split(' ')
			group.append([float(e)for e in arr[0].split(',')])
			labels.append(filter(remove_blank, arr[1]))
	print classify0([0,0], array(group), labels, 3)



