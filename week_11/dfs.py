def DFS(adj_list, s, visited):
    visited[s] = 1
    for v in adj_list[s]:
        if visited[v] == 0:
            DFS(adj_list, v, visited)
    print(s)
