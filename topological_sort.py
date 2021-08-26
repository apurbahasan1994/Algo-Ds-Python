from collections import defaultdict


def topological_sort(graph, vertices):
    ans = []
    stack = []
    visited = [0]*(vertices+1)
    for j in range(1, vertices):
        stack.append(j)
        while stack:
            i = stack[-1]
            visited[i] = True
            if graph[i] is None or graph[i] == []:
                stack.pop()
                if i not in ans:
                    ans.append(i)

            else:
                count = 0
                for child in graph[i]:
                    if visited[child] != 1:
                        visited[child] = 1
                        stack.append(child)
                    else:
                        count += 1
                    if count == len(graph[i]):
                        stack.pop()
                        if i not in ans:
                            ans.append(i)
    ans.reverse()
    print(ans)


def main(arr, vertices):
    graph = defaultdict(list)
    for element in arr:
        graph[element[0]].append(element[1])

    topological_sort(graph, vertices)


main([[1, 3], [2, 3], [2, 4], [3, 5], [4, 6], [5, 7], [5, 6], [6, 8]], 8)
