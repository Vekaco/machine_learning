# -*- coding:utf-8 -*-
# Filename: 1.2.4.py
import numpy as np
#创建3*5的全0矩阵
myZeros = np.zeros([3, 5])
print myZeros

#创建3*5的全1矩阵
myOnes = np.ones([3, 5])
print myOnes

#生成随机矩阵
myRand = np.random.rand(3, 4)#3*4的0～1为元素的随机数矩阵
print myRand

#单位矩阵(方阵）
myEye = np.eye(3)
print myEye

from numpy import *
#矩阵的元素运算
#矩阵元素的+，-，*，/

#（1）矩阵元素相加与相减
# 条件：矩阵的行数和列数必须相同
myOnes = ones(3)
myEye = eye(3)
print myOnes + myEye
print myOnes - myEye
# (2)矩阵数乘
# 条件：矩阵的每个元素都与该数相乘
mymatrix = mat("1,2,3;4,5,6;7,8,9")
a = 10
print a * mymatrix
# (3)矩阵所有元素求和
print sum(mymatrix)
# （4）矩阵各元素的积（矩阵点乘）
# 条件：同维度元素相乘，维度不同时可通过广播规则扩充
mymatrix2 = 1.5 * ones(3)
print np.multiply(mymatrix, mymatrix2)

# (5）矩阵各元素的n次幂
mylist = mat("1,2,3;4,5,6;7,8,9")
print np.power(mylist, 2)

#矩阵乘法
#条件：m*p矩阵a与p*n矩阵b相乘，得到m*n结果矩阵c, c矩阵(i,j)位置元素为a矩阵i行与b矩阵j列各元素乘积之和
mymatrix = mat("1,2,3;4,5,6;7,8,9")
mymatrix2 = mat("1;2;3")
print mymatrix * mymatrix2

#矩阵的转置
#条件：矩阵元素行列互换
mymatrix = mat("1,2,3;4,5,6;7,8,9")
print mymatrix.T
np.transpose(mymatrix)
print mymatrix

#矩阵的其他操作：行列数，切片，复制（浅拷贝、深拷贝），比较
#行列数
mymatrix = mat("1,2,3;4,5,6;7,8,9")
[m, n] = shape(mymatrix)
print "矩阵的行数和列数：",m, n
#按行切片
myscl1 = mymatrix[0]
print "按行切片：", myscl1
#按列切片
myscl2 = mymatrix[:,0]
print "按列切片：", myscl2
#按列切片2
myscl3 = mymatrix.T[0]
print "按列切片：", myscl3
#复制
#浅拷贝
a = mymatrix
#深拷贝
b = np.copy(mymatrix)
#当改变mymatrix元素时，浅拷贝矩阵也会改变其元素，而深拷贝不会改变
mymatrix[0] = mat("7,7,7")
print a
print b
#矩阵比较：会对两个矩阵的各元素依次比较，符合条件为True
print mymatrix < mymatrix.T