# Matplotlib

## 面向函数绘图

### 折线图
```
import numpy as np 
from matplotlib import pyplot as plt 
plt.title()
plt.xlabel()
plt.ylabel()
plt.plot(x, y, '')
plt.show()
```

```
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]
y3 = [1, 8, 27, 64]
y4 = [1, 16, 81, 124]
# 创建一个画布
plt.figure()
# 在figure下线
plt.plot(x, y1, "-o") #实线
plt.plot(x, y2, "--o") #虚线
plt.plot(x, y3, "-.o") #虚点线
plt.plot(x, y4, ":o") # 点线
# 展现画布
plt.show()
```

#### 绘图颜色
![](2022-03-12-17-21-30.png)


### 散点图
x = []; y = []
plt.scatter(x, y)

### 条形图
```
from matplotlib import pyplot as plt 
x =  [5,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis') 
plt.show()
```

### 饼状图
```
import matplotlib.pyplot as plt

# 数据
labels = ["A", "B", "c", "d"]
fracs = [15, 30, 45, 10]


# 画图
plt.pie(x=fracs, labels=labels)

# 展示
plt.show()
```

### 直方图
用于统计数据
注: 正态分布数据生成:
import numpy as np
import random
import matplotlib.pyplot as plt
x = mean + sigma * random.randn(N)


```
import matplotlib.pyplot as plt
import numpy as np

# 数据
mu = 100  # 均值
sigma = 20  # 方差
# 2000个数据
x = mu + sigma*np.random.randn(2000)


# 画图 bins:条形的个数， normed：是否标准化
plt.hist(x=x, bins=10)


# 展示
plt.show()
```

## subplot
subplot(numRows, numCols, plotNum)

布局示例:
1. (211)(212)
2. (211)(223)(224)

subplot2grid((分割)，（起始位置），colspan=列宽, rowspan=行宽)
```
import matplotlib.pyplot as plt

# 创建画布
plt.figure()
# 创建子图
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
ax1.plot([1, 2], [1, 2])
ax1.set_title("No1")
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)
ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)

plt.show()
```
## 面向对象绘图
[^_^]:
    TODO: 尚未掌握有关技能;Figure和FigureCanvas
[https://blog.csdn.net/zchshhh/article/details/78215646](https://blog.csdn.net/zchshhh/article/details/78215646)

plt.figure()  创建窗口

### 动态图
```
import numpy as np
import matplotlib.pyplot as plt


# 数据（画折线至少需要两个点）
xs = [0, 0]
ys = [1, 1]

for i in range(500):
    # 不断更新这个两个点
    y = np.random.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = y
    plt.plot(xs, ys, "b")
    plt.xlim(xs[1]-10, xs[1]+10)
    plt.pause(0.1)

# 显示（暂停）
plt.show()

```