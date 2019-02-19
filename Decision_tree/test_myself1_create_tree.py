#coding=UTF-8
import numpy as np
import matplotlib.pyplot as plt
import math
import operator


#>>> dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'yes'],[0,1,'no'],[0,1,'no'],[1,0,'no']]
#>>> calcShannonEnt(dataSet)
#1.0
#>>> dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'yes'],[0,1,'yes'],[0,1,'no'],[1,0,'no']]
#>>> calcShannonEnt(dataSet)
#0.9182958340544896
#>>> dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'yes'],[0,1,'yes'],[0,1,'yes'],[1,0,'no']]
#>>> calcShannonEnt(dataSet)
#0.6500224216483541
#>>> dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'yes'],[0,1,'yes'],[0,1,'yes'],[1,0,'yes']]
#>>> calcShannonEnt(dataSet)
#0.0

#PR编号           红不红         圆不圆             甜
#1               1         1               yes
#2               1         1               yes
#3               1         0               no
#4               0         1               no
#5               0         1               no
dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
#dataSet=[[1,1,'yes'],[1,0,'yes'],[1,0,'no'],[1,0,'no'],[0,1,'yes'],[0,1,'no']]
labels=['Red','Round']
def calcShannonEnt(dataSet):                            #墒的值只和分类标签的发布概率有关，样本数据的特征没有任何关系
    numEntries = len(dataSet)
    #数据集大小
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]                      #最后一列是分类标签，提取样本数据中的标签
        if currentLabel not in labelCounts.keys():      #建立一个字典，表示样本数据中每类标签的数量，key是标签,value是该标签的数量
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        #每个类中数据个数统计
    shannonEnt = 0.0
    for key in labelCounts: 
        prob = float(labelCounts[key])/numEntries       #计算没类标签占总数量的百分比，也就是概率
        shannonEnt -= prob  * math.log(prob,2)          #根据香农公式计算墒
        #shannonEnt = shannonEnt - prob * math.log(prob,2)
    return shannonEnt                                   #返回墒

a=calcShannonEnt(dataSet)
print a

def splitDataSet(dataSet, axis, value):                 #改函数用来产生一个去掉样本中的某个特征值(axis)=value后的样本数据。
    retDataSet = []                                     #用来存放生产的样本数据
    for featVec in dataSet:                             #按行循环，也就是每个样本循环
        if featVec[axis] == value:                      #如果该列中有这个特征值，也就是说该特征值等于输入的value
            reducedFeatVec = featVec[:axis]             #拷贝出这个特征值前面的元素
            reducedFeatVec.extend(featVec[axis+1:])     #拷贝出这个特征值后面的元素，这样reducedFeatVec就是一个去掉该列后的样本
            retDataSet.append(reducedFeatVec)           #retDataSet就是所有的满足该特征分类=value的元素列表集合，但是不包括该特征列了，因为特征已经被用来分类了
    return retDataSet

def chooseBestFeatureToSplit(dataSet):                  #该函数用来选择出样本数据中的最好的用来分类的特征值。如果调用该函数，然后去掉选出来的特征值，然后接着调用，就会选出第二个号的特征值
    numFeatures = len(dataSet[0]) - 1                   #计算有多少个特征
    baseEntropy = calcShannonEnt(dataSet)               #计算原始数据的信息熵
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):                        #按照样本数据的列循环，也就是按照样本数据中的每个特征循环
        featList = [example[i] for example in dataSet]  #从第一列(第一个特征)开始，生成一个该特征的特征值列表
        print 'featList:'+ str(featList)
        uniqueVals = set(featList)                      #去掉该该列(该特征)中的重复元素(特征值)
        print 'uniqueVals'+ str(uniqueVals)
        newEntropy = 0.0
        print len(uniqueVals)
        if len(uniqueVals) == 1:                        #这里有个Bug，如果不添加这个if判断，那么在只剩下一个特征值对应多个分类标签的时候，就会把分类标签当做最佳特征值返回比如：dataSet=[[1,1,'yes'],[1,0,'yes'],[1,0,'no'],[1,0,'no'],[0,1,'yes'],[0,1,'no']]
            bestFeature=i                               ##############################################################
            continue
        for value in uniqueVals:                        #按照该特征的每个特征值循环，计算按照该特征值分类后的信息熵
            subDataSet = splitDataSet(dataSet, i, value)    #返回一个：该列中的元素等于value（特征=该特征值），并且去掉该列后产生的后的样本数据
            print 'subDataSet:'+str(subDataSet)
            prob = len(subDataSet)/float(len(dataSet))      #计算按照第i列划分，并且元素等于value的样本个数(subDataset少)占总个数(dataSet)的百分比（概率）
            newEntropy += prob * calcShannonEnt(subDataSet) #计算按照第i列划分后的总墒
            print 'newEntropy:' + str(newEntropy)
        infoGain = baseEntropy - newEntropy                 #计算当前分类的信息增益, dataSet的墒减去按照i列划分后的总墒
        print 'infoGain'+str(infoGain)
        if (infoGain > bestInfoGain):                       #比较那种分类的信息增益最大并返回
            print '(infoGain > bestInfoGain)'
            bestInfoGain = infoGain
            print 'bestInfoGain:'+str(bestInfoGain)
            bestFeature = i
            print 'i:'+ str(i)                                      
    return bestFeature                                      #返回可以用来划分的最好的特征值索引


a=chooseBestFeatureToSplit(dataSet)
print a
print '--------------------------------------------------------------'


def majorityCnt(classList):                     #按照所有特征分类完成之后，在同一个特征下，还会有不少样本有不同的分类标签。这时候只能采取少数服从多数的原则，返回最多的分类标签
    classCount={}                               #创建一个类标签的字典
    for vote in classList:                      #遍历输入的类标签列表中每一个元素
        #如果元素不在字典中
        if vote not in classCount.keys():       #在字典中添加新的键值对(这种方法同直接使用字典的方法has_key和get效率高)
            classCount[vote]=0
        classCount[vote]+=1                     #否则，当前键对于的值加1
        #对字典中的键对应的值所在的列，按照又大到小进行排序,classCount.items 列表对象（键值对），key=operator.itemgetter(1) 获取列表对象的第一个域的值（第零个key，第一个是value），reverse=true 降序排序，默认是升序排序
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]               #返回出现次数最多的类标签

def createTree(dataSet,labels):                                     #输入参数为样本数据集，每个特征的特征名称列表
    classList=[example[-1] for example in dataSet]                  #创建一个列表，列表元素为样本中的最后一列，也就是分类标签列表
    print 'dataSet:'+str(dataSet)
    print 'classList:'+str(classList)
    if classList.count(classList[0])==len(classList):               #如果上面创建的分类标签列表中的第一个元素个数就等于这个列表中的元素个数，说明这个列表中没有别的分类了
        print 'classList.count(classList[0])==len(classList)'
        return classList[0]                                         #返回该分类标签
    if len(dataSet[0])==1:                                          #满足该条件的话，说明dataSet只剩下最后一列（标签列），没有特征值了，也就是说只能做叶子。
        print 'len(dataSet[0])==1'
        return majorityCnt(classList)                               #剩下的标签按照少说服从多数的原则，得出该叶子应该用哪种标签
    bestFeat=chooseBestFeatureToSplit(dataSet)                      #计算出针对dataSet分类的最好的特征索引
    bestFeatLabel=labels[bestFeat]                                  #根据这个索引得到特征的名字
    myTree={bestFeatLabel:{}}                                       #创建字典的，key=该特征的名字（也就是说创建了树的节点）
    print 'myTree:'+str(myTree)
    subLabels=labels[:]                                             #复制特征名称列表
    del(subLabels[bestFeat])                                        #删除刚才已经用过的特征的名字（刚才已经用被删除的特征名字创建了一个字典）
    featValues=[example[bestFeat] for example in dataSet]           #按照最好的特征索引，创建出该特征的特征值列表
    uniqueVals=set(featValues)                                      #去掉该特征中的重复的特征值
    for value in uniqueVals:                                        #按照该特征中特征值循环
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

myTree=createTree(dataSet,labels)
print myTree
