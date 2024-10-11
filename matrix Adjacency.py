def AdjacencyList(ver,edges):
    di={}
    for u,v in edges:
        if u not in di.keys():
            di[u]=[v]
        else:
            di[0].append(v)
    for u,v in di.items():
        print(u,"->",v)

ver=int(input())
edg=int(input())
edges=[]
for i in range(edg):
    edges.append(list(map(int,input("Enter edges or path").split())))
AdjacencyList(ver,edg)
