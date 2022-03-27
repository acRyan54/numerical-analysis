# NumPy

1. a.reshape() 返回的是非拷贝副本，即改变返回后数组的元素，原数组对应元素的值也会改变
2. **喜欢我ndarray吗?**np.dtype('name', 'i4'), 建立数组时候np.array(object, dtype = xxx)可以限定列的类型，并可以通过ndarray['key']的方式取出列

np.empty(shape, dtype); np.ones(); np.frombuffer(b'xxx', dtype); np.fromiter(iter, dtype)

np.arange(start, stop, step, dtype)

`生成数列`
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)

`切片`
s = slice(start, stop, step); a[s]
多维情况 a[行slice, 列slice], a[..., 1]
`整数索引`
示例:获取矩阵四角元素
```[python]
import numpy as np 
 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]  
print  ('这个数组的四个角元素是：')
print (y)

z = x[[0, 0, 3, 3], [0, 2, 0, 2]].reshape(2,2)
print(z)
```
即有x[[ [0, 0], [3, 3] ] , [ [0, 2], [0, 2] ]  ] == x[[0, 0, 3, 3], [0, 2, 0, 2]].reshape(2,2)


`过滤`
a[a > 5]; a[~np.isnan(a)]; a[np.iscomplex(a)]

`花式索引`
a[[1,3,2], ...]; a[..., [1,3,2]];
x[np.ix_([1,5,7,2],[0,3,1,2])]  会遍历行/列序号生成4*4矩阵

3. numpy和list类型的转换: 
   np.map(l); np.array(a);     a.tolist()

4. brocast规则: A+B == A+ np.tile(B, (4, 1))
5. **np.nditer**顺序 order = 'F'列优先; order = 'C'行优先; order = 'A'原顺序

b = a.copy(order = 'F')
for x in np.nditer(a, order = 'F'):
for x in np.nditer(a, op_flags=['readwrite']):

``` 示例:修改每个元素
import numpy as np
 
a = np.arange(0,60,5) 
a = a.reshape(3,4)  
print ('原始数组是：')
print (a)
print ('\n')
for x in np.nditer(a, op_flags=['readwrite']): 
    x[...]=2*x    # 注:这里的[...]很关键
print ('修改后的数组是：')
print (a)
```
![](2022-03-11-15-36-23.png)

``` 示例:输出各列list
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):  
   print (x, end=", " )
```

6. flags =  ['external_loop'] 在nditer的order与数组相同时顺序打印,反向时打印多个一维数组; 
7. x[...]是修改numpy的元素, 而x只是迭代器的拷贝

`数组操作`
np.reshape(arr, newshape, order='C') 或者 a.reshape
a.flat 返回迭代器;   a.flatten(order = 'A')返回一个展开的数组
np.transpose(a) == a.T == a.transpose()

8. 对a.flatten()修改不影响原数组, a.ravel()会影响
****
`广播`
numpy.broadcast_to(array, shape) 返回广播的结果数组
```
a = np.arange(4).reshape(1, 4)
np.broadcast_to(a, (4, 4))
```

numpy.squeeze(arr, axis) 删除一维的条目
注意：只有size为1的axis可以删除

`连接数组`
numpy.concatenate((a1, a2, ...), axis); axis默认为0
np.stack((*arr), axis); 
np.hstack((*arr), axis) 水平堆叠
np.vstack((*arr), axis) 垂直

`切割数组`
numpy.split(ary, indices_or_sections, axis); 切割的位置可以是list,可以是n平均
np.hsplit()
np.vsplit()

numpy.append(arr, values, axis=None)
numpy.insert(arr, obj, values, axis)
Numpy.delete(arr, obj, axis)
若不声明axis,则默认都是展开

9. 二进制运算 & | ~ ^ >> <<  
np.bitwise_and(); .bitwise_or(); .left_shift(); .right_shift();
.invert()  补码

10. 进制转换: bin(), oct(), hex() 返回带有0b,0o,0x标识str;  np.binary_repr(num, width) 返回正常的二进制数字
11. 字符串

![](2022-03-12-15-52-02.png)
print (np.char.center('Runoob', 20,fillchar = '*'))
print (np.char.split ('www.runoob.com', sep = '.'))

`数组计算`  按位运算
add(), subtract(), multiply(), divide(), mod(); 满足brocast条件才可
np.reciprocal(a) 返回倒数
np.power(a, b); np.power(a, 3)

`统计函数`
numpy.amin(a, axis=None) 用于计算数组中的元素沿指定轴的最小值。
numpy.amax() 用于计算数组中的元素沿指定轴的最大值。
numpy.ptp()极差
numpy.percentile()接受以下参数numpy.percentile(a, q, axis): 第 p 个百分位数是这样一个值，它使得至少有 p% 的数据项小于或等于这个值，且至少有 (100-p)% 的数据项大于或等于这个值。

numpy.median() 函数用于计算数组 a 中元素的中位数（中值)
注:中位数可以用np.percentile(a, 50, axis)
numpy.mean()平均
numpy.average(a, weights)加权平均
        print (np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True))
numpy.std(a, axis)标准差
numpy.var(a, axis)方差

`排序和筛选`
numpy.sort(a, axis, kind = 'quicksort', order); order一般用于dtype的字段
numpy.argsort() 函数返回的是数组值从小到大的**索引**值
.argmax(), .argmin()
.nonzero()

np.where(x >  3) 返回满足条件的索引
**用bool_array对比**numpy.extract(a, condition) 函数根据某个条件从数组中抽取元素，返回满条件的元素

y = np.argsort(x);  x[y];  按照索引重构数组

```
import numpy as np 
 
x = np.arange(9.).reshape(3,  3)  
print ('我们的数组是：')
print (x)
# 定义条件, 选择偶数元素
condition = np.mod(x,2)  ==  0  
print ('按元素的条件值：')
print (condition)
print ('使用条件提取元素：')
print (np.extract(condition, x))
```

12. 副本是一个数据的完整的拷贝，如果我们对副本进行修改，它不会影响到原始数据，物理内存不在同一位置。

视图是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。
np.view() 操作改变原数组
np.copy() 完全不影响

13. 矩阵
    
import numpy.matlib
[](https://www.runoob.com/numpy/numpy-matrix.html)
numpy.matlib.empty(shape, dtype, order)

numpy.matlib.eye(n, M,k, dtype) 不一定是方阵; k: 对角线的索引
numpy.matlib.identity(n, dtype)

numpy.matlib.rand()

`array和matrix转换`
i = np.matrix('1,2;3,4')
j = np.asarray(i)
k = np.asmatrix (j)

#### np.linalg  计算可以直接对array进行

np.dot()
np.inner() 向量内积
np.matmul() 矩阵乘积
np.linalg.det()
np.linalg.solve(A, b)  Ax = b
np.linalg.inv()

```
import numpy as np 
 
a = np.array([[1,1,1],[0,2,5],[2,5,-1]]) 
 
print ('数组 a：')
print (a)
ainv = np.linalg.inv(a) 
 
print ('a 的逆：')
print (ainv)
 
print ('矩阵 b：')
b = np.array([[6],[-4],[27]]) 
print (b)
 
print ('计算：A^(-1)B：')
x = np.linalg.solve(a,b) 
print (x)


y = np.matmul(ainv, b)
print(y)
# 这就是线性方向 x = 5, y = 3, z = -2 的解
```
