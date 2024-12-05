# Name: Bryce Worley
# GitHub: Bryce-Worley
# Description:  Program defines a function that returns the shortest path from a source node to a destination node in a
#               2-D Matrix with certain cells 'walled-off'. The program implements a BFS with a dequeue data structure.

from collections import deque


def solve_puzzle(Board, Source, Destination):
    """
    Returns the shortest path from Source to Destination for a given 2-D matrix, Board.

     :param Board:      A 2-d Matrix where '-' represents an open cell and '#' represents a walled cell.
                            E.g.['-', '-', '-', '-', '-'],
                                ['-', '-', '#', '-', '-'],
                                ['-', '-', '-', '-', '-'],
                                ['#', '-', '#', '#', '-'],
                                ['-', '#', '-', '-', '-']
    :param Source:      A tuple representing a starting node on Board. E.g (row, column)
    :param Destination: A tuple representing a starting node on Board. E.g (row, column)
    :return:            A list of tuples representing the path from Source to Destination
    """
    # Edge case: source and destination are the same
    if Source == Destination:
        return [Source]

    # Initialize [n] and [m] as cols and rows respectively
    cols = len(Board[0])
    rows = len(Board)

    # Initialize a 'visited' set to track nodes already processed.
    visited = set([Source])

    # Initialize a deque with [(Source, Path)]. Let Path get [Source] as starting point.
    # Idea for deque found at https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    queue = deque([(Source, [Source])])

    # While there are nodes to process in the deque, continue BFS
    while queue:
        current_vertex, current_path = queue.popleft()

        # For-loop iterates through possible valid moves from the current node and
        # update queue and visited if a valid move exists. If move reaches Destination, return path.
        for row, col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_row, neighbor_col = current_vertex[0] + row, current_vertex[1] + col

            if (rows > neighbor_row >= 0 and cols > neighbor_col >= 0 and Board[neighbor_row][neighbor_col] == '-' and
                    (neighbor_row, neighbor_col) not in visited):
                if (neighbor_row, neighbor_col) == Destination:
                    return current_path + [(neighbor_row, neighbor_col)]
                queue.append(((neighbor_row, neighbor_col), current_path + [(neighbor_row, neighbor_col)]))
                visited.add((neighbor_row, neighbor_col))

    # No path exists; return None
    return None


if __name__ == '__main__':
    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]

    print(solve_puzzle(puzzle, (0,2), (2,2)))
    print(solve_puzzle(puzzle, (0,0), (4,4)))
    print(solve_puzzle(puzzle, (0,0), (4,0)))
    print(solve_puzzle(puzzle, (0,0), (0,0)))
    print(solve_puzzle(puzzle, (4,4), (0,0)))

