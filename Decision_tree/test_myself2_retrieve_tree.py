#coding=UTF-8
import numpy as np
import matplotlib.pyplot as plt
import math
import operator


#@intputTree 构建好的决策树
#@featLabels 特征标签列表
#@testVec 测试实例
def classify(inputTree,featLabels,testVec):
    #找到树的第一个分类特征，或者说根节点'no surfacing',注意python2.x和3.x区别，2.x可写成firstStr=inputTree.keys()[0], 而不支持3.x
    firstStr=list(inputTree.keys())[0]                      #得到根节点
    featIndex=featLabels.index(firstStr)                    #得到该节点对应的特征标签索引，也就是要知道从测试数据的第几个特征开始分类

    secondDict=inputTree[firstStr]                          #得到该节点的分支
    #遍历分类特征所有的取值

    if testVec[featIndex] not in secondDict.keys():         #这里有个Bug，如果测试实例的某个特征值不在分支中，程序处理会有问题，所以增加了这两行代码。目的是为了在这种情况下默认返回该节点下面的第一个分支。
        classLabel=secondDict.values()[0]                   #########################################################
    for key in secondDict.keys():                           #遍历该节点的分支节点
        if testVec[featIndex]==key:                         #如果测试实例的第几个特征值（根据该节点对应的特征标签索引）等于key，就继续
            if type(secondDict[key]).__name__=='dict':      #如果该节点的分支还是字典，也就是说还是节点，则继续递归
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]                  #如果是叶子节点，则返回节点的值（分类标签）

    return classLabel


#Tree={'Round': {0: {'Red': {0: 'no', 1: 'yes'}}, 1: 'yes'}}
Tree={'Red': {0: 'no', 1: {'Round': {0: 'no', 1: 'yes'}}}}
labels=['Red','Round']
#PR编号           红不红         圆不圆             甜
#1               0         1          
dataSet=[0,1]

result=classify(Tree,labels,dataSet)
print result
