

def dijkstra(graph, s):
    visited = [0] * len(graph) # [0, 0, 0, 0, 0]
    dists = [1e10] * len(graph) # [inf, inf, inf, inf, inf]    
    dists[s] = 0

    while 0 in visited:
        min_d = 1e17
        min_d_node = -1
        for i in range(len(dists)):
            if visited[i] == 0 and dists[i] < min_d:
                min_d = dists[i]
                min_d_node = i

        for v in range(len(graph[min_d_node])):
            if dists[v] > dists[min_d_node] + graph[min_d_node][v] and visited[v] == 0 and graph[min_d_node][v] != 0:  
                dists[v] = dists[min_d_node] + graph[min_d_node][v]
        visited[min_d_node] = 1
    return dists


graph = [
    [0, 10, 0, 10, 20],
    [10, 0, 10, 0, 40],
    [0, 10, 0, 30, 5],
    [10, 0, 30, 0, 0],
    [20, 40, 5, 0, 0],
]

dists = dijkstra(graph, 0)
print(dists)