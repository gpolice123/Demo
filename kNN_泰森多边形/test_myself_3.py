#coding=UTF-8
import numpy as np
from os import listdir
import operator
#import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm              #颜色管理包


def createDataSet():
    group=np.random.randint(15,size=(15,2))         #生成15组从1到10的随机坐标，产生一个10行2列的列表
    labels=['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    #数组的排序
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        #在字典中添加key对应的value，如果有就加一，没有就创建但是值为0
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

number = 2000
vote = 1
#x= np.random.normal(0,1,number)
#y= np.random.normal(0,1,number)
#x= np.random.random(number)
#y= np.random.random(number)
x= np.random.random(number)*15
y= np.random.random(number)*15
group,labels=createDataSet()

#data_label=calsssify0([0,0],group,labels,3)

fig=plt.figure()
ax=fig.add_subplot(111, facecolor='white')


cmap=cm.rainbow(np.linspace(0.0, 1.0, len(labels)))     #产生一个长度为len(labels)的颜色种类
#np.linspace产生一个起点为0，终点为1，等分为len(labels)的一维数组
#cm.ranbow根据输入的数组产生对应的颜色，颜色之前的差别为对应数组元素之间的差别
for i in range(number):
    data_label=classify0([x[i],y[i]],group,labels,vote)
    ax.scatter(x[i],y[i],c=cmap[labels.index(data_label)])
'''    
#    plt.annotate(data_label,xy=(x[i],y[i]))
    if data_label=='A':
        ax.scatter(x[i],y[i],c=cmap[0])                 #从cmap的颜色种类中选取第一个颜色
    elif data_label=='B':
        ax.scatter(x[i],y[i],c=cmap[1])
    elif data_label=='C':
        ax.scatter(x[i],y[i],c=cmap[2])
    elif data_label=='D':
        ax.scatter(x[i],y[i],c=cmap[3])
    elif data_label=='E':
        ax.scatter(x[i],y[i],c=cmap[4])
    elif data_label=='F':
        ax.scatter(x[i],y[i],c=cmap[5])
    elif data_label=='G':
        ax.scatter(x[i],y[i],c=cmap[6])
    elif data_label=='H':
        ax.scatter(x[i],y[i],c=cmap[7])
    elif data_label=='I':
        ax.scatter(x[i],y[i],c=cmap[8])
    else:
        ax.scatter(x[i],y[i],c=cmap[9])
'''
ax.scatter(group[:,0],group[:,1])                   #锚点最后画，不然会被背的颜色覆盖
for i,txt in enumerate(group):
    plt.annotate(labels[i],xy=(group[i,0],group[i,1]))    


plt.show()
