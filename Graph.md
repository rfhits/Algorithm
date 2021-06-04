# Graph

## Prim

[Prim算法详解](https://www.cnblogs.com/ggzhangxiaochao/p/9070873.html)

### 目的

最小生成树。

给一个（无向）连通图，找一棵树，这个树也是个连通的子图，这个树各个边的权和最小。

### 实际应用

为一个城市群，建立相互连通的公路；建立最短的、能互相通信的通道。

### 核心思想

每次只找一条边，一条可连通的，最“短”的边

### 简单描述

1. 输入：一个加权连通（无向）图，其中顶点集合为V，边集合为E；
2. 初始化：Vnew = {x}，其中x为集合V中的任一节点（起始点）
3. 重复下列操作，直到Vnew = V：
   在集合E中选取和Vnew中的**元素接连**、且权重最小的边，注意新边的俩个点不能在Vnew中
   如果存在有多条满足前述条件即具有相同权值的边，则可任意选取其中之一
   将此边所接连的新的点加入集合Vnew中，
4. 输出：使用集合Vnew和Enew来描述所得到的最小生成树。

Prim可以不用管挑的边会不会导致成环，因为每次都会挑一个新的点进来。

具体的应用，见[最低消耗](/0-OnlineJudge/13-2020秋季第十一次练习/1-最低消耗.py)。

## Welch_Powell

给图找匹配。

1) 将图 G 中的结点按度数递减的次序进行排列(相同度数的结点的排列随意)。
2) 用第一种颜色，对第一点着色，并按排列次序对与前面结点不相邻的每一点着同样的颜色。
3) 用第二种颜色对尚未着色的点重复第2 步, 直到所有的点都着上颜色为止。

[韦尔奇.鲍威尔法(Welch Powell)](https://www.cnblogs.com/dystopia-p/archive/2013/04/17/3025908.html)