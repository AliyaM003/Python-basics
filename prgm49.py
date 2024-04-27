//DFS
def initiateDFS(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFS(neighbour, visited, adj, result)
 
 
def printDFSTraversal(adj, n):
    result = []
    visited = [False] * n 
 
    for i in range(n):
        if visited[i] == False:
            initiateDFS(i, visited, adj, result)
 
    print("DFS traversal is:", result)
 
# adjacency list construction
 
n, m = map(int, input().split())
adj = []
for i in range(n): 
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
printDFSTraversal(adj, n)

#INPUT:11 10
#0  1
#0 2  
#0 3
#1 4
#4 6
#4 5
#7 8
#7 9
#9 10
#8 10
#DFS traversal is: [0, 1, 4, 6, 5, 2, 3, 7, 8, 10, 9]
