# Prim: select vertex, do not need to judge loop
# data sample
##V = ['a', 'b', 'c']
##E = [(1, 'a', 'b'), (2, 'b', 'c'), (5, 'a', 'c')]

def Prim(V, E):
    V_added = [V[0]]
    E_added = []
    E_can_choose = []
    E_last = E[:]
    while len(E_added) != len(V) - 1:
        # updata edges_can_choose
        for e in E_last:
            if e[1] in V_added and e[2] in V_added:
                pass
            else:
                E_can_choose.append(e)
        E_can_choose.sort(key=lambda x: x[0])
        e = E_can_choose[0]
        E_added.append(e)
        E_last.remove(e)
        if e[1] in V_added:
            V_added.append(e[2])
        else:
            V_added.append(e[1])
        E_can_choose.clear()
    return E_added


V = ['a', 'b', 'c', 'd', 'e', 'f']
E = [(1, 'a', 'b'), (9, 'a', 'c'), (2, 'a', 'd'),
     (8, 'b', 'c'), (5, 'b', 'e'), (4, 'b', 'f'),
     (7, 'c', 'd'),
     (6, 'd', 'e'), (3, 'd', 'f'),
     (10, 'e', 'f')]
E_added = Prim(V, E)
print(E_added)
