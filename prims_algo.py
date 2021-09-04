from collections import defaultdict


def prims(graph, n):
    queue = []
    visited = []
    cost = [999]*(n+1)
    cost[1] = 0
    queue.append(1)
    for i in range(n):
        min_cost = 999
        min_inx = None
        for j in range(1, len(cost)):
            if j not in visited and cost[j] < min_cost:
                min_cost = cost[j]
                min_inx = j

        if not min_inx:
            break

        for adj in graph[min_inx]:
            if adj[0] not in visited:
                if cost[adj[0]] > adj[1]:
                    cost[adj[0]] = adj[1]
                    visited.append(min_inx)
    print(cost)


def main(arr, n):
    graph = defaultdict(list)
    for v in arr:
        graph[v[0]].append([v[1], v[2]])
        graph[v[1]].append([v[0], v[2]])
    prims(graph, n)


main([[1, 2, 10], [1, 3, 20], [2, 3, 30], [2, 4, 5], [3, 4, 15], [
     3, 5, 6], [4, 5, 8]], 5)
