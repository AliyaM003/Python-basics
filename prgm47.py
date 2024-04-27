//GRAPHS
n,m= map(int,input().split())
#construct matrix of size n*n
#n=4
adj = []
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    adj.append(row)
        #adj = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
           
for i  in range(m):
     #2 5
     u,v = map(int,input().split())
     adj[u][v]=1
     adj[v][u]=1
print(adj)

//INPUT
6 7
0 1
0 2
0 3
1 0   
1 5
2 5
2 3 

//OUTPUT
[[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0]]

