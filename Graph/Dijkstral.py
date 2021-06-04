# 算法详解：
# https://www.zhihu.com/question/20972566/answer/290944499

# 数据结构说明：
# E是Edges的集合，(weight, vertex, vertex)
# 如：
# V = ['a', 'b', 'c']
# E = {(4, 'a', 'b'), (1, 'a', 'c'), (2, 'c', 'b')}
# 从起点到每个点的距离放在一个叫做Dst的Dict里，
# 如：
# {'u1': 0, 'u2': 3, 'u3': 2, 'u4': 3}
# pre存储最短路径视图下，每个点的pre是谁。


def Dijstral(V, E, v0, pre_Dict):
    """给定V、E和起始顶点，给出最短路径长度"""
    # 在Dst中选一个最小的点（此点不在N中）
    # 然后添加到N中，并且更新Dst
    pre_Dict[v0] = v0
    if v0 not in V:
        print("the vertex not in Graph")
        return
    N = []
    inf = 10000
    Dst = dict()
    for v in V:
        Dst[v] = inf
    Dst[v0] = 0
    sortedDst = None
    ancher = None
    while sorted(N) != sorted(V):
        sortedDst = sorted(Dst.items(), key=lambda x: x[1])
        for (v, d) in sortedDst:
            if v in N:
                pass
            else:
                # 成功拿到第一个不在N中，并且dst最小的v
                # 取名为anchor
                N.append(v)
                ancher = v
                break

        # 根据edges刷新Dst
        for (w, x, y) in E:
            if x == ancher and w + Dst[x] < Dst[y]:
                Dst[y] = w + Dst[x]
                pre_Dict[y] = x
            # 因为是有向图，所以注释掉这一段
            # elif y == ancher and w + Dst[y] < Dst[x]:
            #     Dst[x] = w + Dst[y]
            else:
                pass

    return Dst


def get_path(pre_Dict, vn):
    """给定pre_dict和终点，返回list路径"""
    v0 = None
    for key in pre_Dict.keys():
        # 找到起点
        if pre_Dict[key] == key:
            v0 = key
            break
        else:
            pass

    # 先把终点放到list尾巴上
    path = [vn]
    v = vn
    while v != v0:
        path.insert(0, pre_Dict[v])
        # 逐个回溯
        v = pre_Dict[v]
    return path


# V = ['a', 'b', 'c']
# E = {(4, 'a', 'b'), (1, 'a', 'c'), (2, 'c', 'b')}


# V = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8']
# E = {(4, 'a', 'b'), (2, 'a', 'd'), (3, 'b', 'c'), (3, 'b', 'e'),
#      (2, 'c', 'z'), (3, 'd', 'e'), (1, 'e', 'z')}


V = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8']
E = {(5, 'u1', 'u2'), (2, 'u1', 'u3'), (3, 'u1', 'u4'), (6, 'u2', 'u5'),
     (1, 'u3', 'u2'), (7, 'u3', 'u5'), (3, 'u3', 'u6'), (1, 'u3', 'u7'),
     (6, 'u4', 'u3'), (1, 'u4', 'u7'), (5, 'u5', 'u8'),
     (1, 'u6', 'u5'), (9, 'u6', 'u8'),
     (3, 'u7', 'u6'), (11, 'u7', 'u8')}

# pre中以键值对的方式存储了在最短路径的视图下，
# 每个点的前一个点是谁
pre_Dict = {}
Dst = Dijstral(V, E, 'u1', pre_Dict)
print(Dst)
for key in pre_Dict.keys():
    print(key, ':', pre_Dict[key])
path = get_path(pre_Dict, 'u8')
print(path)
