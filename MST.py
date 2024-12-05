# Name: Bryce Worley
# GitHub: Bryce-Worley
# Description:  Program defines a functions that returns a minimum spanning tree for a given adjacency matrix.
#               The function adapts Prim's Algorithm to be implemented with a min-heap priority queue.

import heapq


def Prims(G):
    """
    Returns minimum spanning tree for Graph G using Prim's Algorithm implemented with a priority queue

    :param G:   an adjacency matrix
    :return:    list of tuples(v1, v2, weight) that form the mst
    """
    nodes = len(G)

    # Initialize a MST
    mst = []

    # Initialize a 'visited' array with False values to track nodes already processed.
    visited = [False] * nodes
    visited[0] = True

    # Initialize a priority queue with tuple (weight, v1, v2) to access minimum weights
    pq = [(0,0,0)]

    # While there are nodes to process in the priority queue, continue BFS
    while len(pq) > 0:
        weight, v1, v2 = heapq.heappop(pq)
        if visited[v2] is False:
            visited[v2] = True
            mst.append((v1, v2, weight)) # (v1, v2, weight) tuple specified return format

        # For-loop iterates through v2's neighbors
        for node, edge in enumerate(G[v2]):
            if edge != 0 and visited[node] is False:
                heapq.heappush(pq, (edge, v2, node))

    return mst

if __name__ == '__main__':
    input = [
        [0, 8, 5, 0, 0, 0, 0],
        [8, 0, 10, 2, 18, 0, 0],
        [5, 10, 0, 3, 0, 16, 0],
        [0, 2, 3, 0, 12, 30, 14],
        [0, 18, 0, 12, 0, 0, 4],
        [0, 0, 16, 30, 0, 0, 26],
        [0, 0, 0, 14, 4, 26, 0]
    ]

    print(Prims(input))
