
# Kruskal算法，先将边的权重排序，然后按顺序加进去
# 只要这个边加进去后不成环，就能加进去
# 知道加出一个连通图：len(V) = len(E) + 1

# data sample
# V = ['a', 'b', 'c']
# E = [(1, 'a', 'b'), (2, 'b', 'c'), (5, 'a', 'c')]


def find_parent(x):
    global V, parents
    i = V.index(x)  # get x index
    p = parents[i]
    if p == -1:
        return x
    else:
        return find_parent(p)  # find x's parent's parent


def Kruskal(V, E):
    """E is sorted, return Edges seleted"""
    E_added = []
    V_added = []
    global parents
    for (w, u, v) in E:
        if u in V_added and v in V_added:
            if find_parent(u) == find_parent(v):
                pass
            else:
                E_added.append((w, u, v))
                i = V.index(u)
                parents[i] = find_parent(v)
        elif u in V_added and v not in V_added:
            V_added.append(v)
            i = V.index(v)
            parents[i] = u
            E_added.append((w, u, v))
        elif u not in V_added and v in V_added:
            V_added.append(u)
            i = V.index(u)
            parents[i] = v
            E_added.append((w, u, v))
        else:
            E_added.append((w, u, v))
            V_added.append(u)
            V_added.append(v)
            i = V.index(u)
            parents[i] = v

        if len(E_added) == len(V)-1:
            break
        else:
            continue
    return E_added


V = ['a', 'b', 'c', 'd', 'e', 'f']
E = [(1, 'a', 'b'), (9, 'a', 'c'), (2, 'a', 'd'),
     (8, 'b', 'c'), (5, 'b', 'e'), (4, 'b', 'f'),
     (7, 'c', 'd'),
     (6, 'd', 'e'), (3, 'd', 'f'),
     (10, 'e', 'f')]

E.sort(key=lambda x: x[0])
parents = [-1 for i in V]
print(parents)
print(Kruskal(V, E))
print(parents)
