def BFS(adj_list, s):
    visited = [0] * len(adj_list)
    visited[s] = 1
    queue = []
    queue.append(s)

    while queue != []:
        s = queue.pop(0)
        print(s, end=" ")
        for node in adj_list[s]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1
