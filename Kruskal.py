# Kruskal，选择权重最小的边添加，直到连通

# 数据结构说明：
# E是Edges的list，(weight, vertex, vertex)
# 如：
# V = ['a', 'b', 'c']
# E = 




def is_cycled(V, E, u0, v0):
    tv = False
    Vc = {u0, v0}
    Ec = {(u0, v0)}
    n = 0
    while(n != len(Vc)):
        n = len(Vc)
        for (w, u, v) in E:
            if((u in Vc) and (v in Vc)):
                tv = True
                return tv
            if (u in Vc and v not in Vc) or (u not in Vc and v in Vc):
                Ec = Ec | {(u, v)}
                Vc = Vc | {u, v}
                E = E-{(w, u, v)}
                break
    return tv


def Kruskal_span_tree(V, E):
    E = sorted(E)
    Vt = set({})
    Et = set({})
    n = len(V)
    k = 0
    i = 0
    while(len(Et) < n-1):
        [w, u, v] = E[i]
        i = i+1
        if(((u in Vt) and (v in Vt))):
            if(is_cycled(Vt, Et, u, v)):
                continue
        Et = Et | {(w, u, v)}
        Vt = Vt | {u, v}
    return [Vt, Et]
