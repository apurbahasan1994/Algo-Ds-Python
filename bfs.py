from collections import defaultdict


def bfs(graph, V):
    visited = [0]*(V+1)
    queue = []
    queue.append(1)
    while queue:
        vertex = queue.pop(0)
        visited[vertex] = 1
        print(vertex)
        for adjecents in graph[vertex]:
            if not visited[adjecents]:
                queue.append(adjecents)
                visited[adjecents] = 1


def main(arr, V):
    graph = defaultdict(list)
    for element in arr:
        graph[element[0]].append(element[1])
        graph[element[1]].append(element[0])

    bfs(graph, V)


main([[1, 3], [1, 4], [2, 3], [2, 4], [1, 5]], 5)
