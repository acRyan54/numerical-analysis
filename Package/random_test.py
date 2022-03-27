import random

print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)


# 产生随机数列的方法:
### 1
import random
random.sample(range(1, 100), 10)
### 2
import numpy as np  
np.random.random(10) #生成array
np.random.randint(0,10) #一个数
np.random.randint(0,10, 8) #array
### 3
import numpy as np  
x = np.random.randn(1000) # 正态分布