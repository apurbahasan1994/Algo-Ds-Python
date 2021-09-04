def find_parent(node, parent):
    if parent[node] == -1:
        return node
    else:
        parent[node] = find_parent(parent[node], parent)
        return parent[node]


def union(node1, node2, rank, parent):
    parent1 = find_parent(node1, parent)
    parent2 = find_parent(node2, parent)
    if parent1 == parent2:
        return "Cycle"
    else:
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
            rank[parent1] += 1

        elif rank[parent1] < rank[parent2]:
            parent[parent1] = parent2
            rank[parent2] += 1
        else:
            parent[parent2] = parent1
            rank[parent1] += 1
        return "No cycle"


def disjoint_set(edge_list, parent, rank):
    for edge in edge_list:
        ans = union(edge[0], edge[1], rank, parent)
        if(ans == 'Cycle'):
            print(f"Cycle while joining {edge[0]} {edge[1]}")
            break
        else:
            print(f"joined {edge[0]} {edge[1]}")


def main(edge_list, n):
    parent = [-1]*(n+1)
    rank = [0]*(n+1)
    disjoint_set(edge_list, parent, rank)


edge_list = [[0, 1], [2, 3], [1, 2], [0, 4], [4, 3]]
main(edge_list, 5)
