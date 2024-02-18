""" 
Task 2.
- Implement breadth-first search
- Test breadth-first search path 1 => 9
- Test breadth-first search with various starting and ending positions
- Compare breadth-first search with depth-first search
"""

from graph import GRAPH
from test import test, compare_tests, random_node, display
from task1 import dfs_stack, dfs_recurse

def bfs_recurse(graph, start, end, visited):
    siblings = [start] + graph[start]
    unexplored = [x for x in siblings if x not in visited]

    for sibling in unexplored:
        visited.append(sibling)
        if sibling is end:
            return visited

    for sibling in unexplored:
        found_path = bfs_recurse(graph, sibling, end, visited)
        if found_path:
            return found_path

def bfs_queue(graph, start, end, visited):
    queue = [start]

    while queue:
        root = queue.pop(0)
        if root in visited:
            continue

        visited.append(root)

        if root is end:
            return visited

        siblings = graph[root]
        queue.extend(siblings)

if __name__ == "__main__":
    # Test BFS 1 => 9
    test1 = display(test(bfs_recurse, GRAPH, 1, 9))
    test2 = display(test(bfs_queue, GRAPH, 1, 9))
    compare_tests('1=>9 bfs stack vs recurse', test1, test2)

    recurse_tests = []
    queue_tests = []

    for start in GRAPH.keys():
        for end in GRAPH.keys():
            recurse_tests.append(test(bfs_recurse, GRAPH, start, end))
            queue_tests.append(test(bfs_queue, GRAPH, start, end))

    compare_tests('all bfs combinations recurse', *recurse_tests)
    compare_tests('all bfs combinations queue', *queue_tests)
    compare_tests('all bfs combinations recurse vs queue', *recurse_tests, *queue_tests)

    # Test random paths
    recurse_tests = []
    queue_tests = []

    for _ in range(10000):
        start = random_node(GRAPH)
        end = random_node(GRAPH)

        queue_tests.append(test(bfs_queue, GRAPH, start, end))
        recurse_tests.append(test(bfs_recurse, GRAPH, start, end))

    compare_tests('random bfs recurse', *recurse_tests)
    compare_tests('random bfs queue', *queue_tests)
    compare_tests('random bfs recurse vs queue', *recurse_tests, *queue_tests)

    # Compare DFS vs BFS
    dfs_recurse_tests = []
    dfs_iterational_tests = []
    bfs_recurse_tests = []
    bfs_iterational_tests = []

    for _ in range(10000):
        start = random_node(GRAPH)
        end = random_node(GRAPH)

        dfs_recurse_tests.append(test(dfs_recurse, GRAPH, start, end))
        dfs_iterational_tests.append(test(dfs_stack, GRAPH, start, end))

        bfs_recurse_tests.append(test(bfs_recurse, GRAPH, start, end))
        bfs_iterational_tests.append(test(bfs_queue, GRAPH, start, end))

    compare_tests('BFS vs DFS', *dfs_recurse_tests, *dfs_iterational_tests, *bfs_recurse_tests, *bfs_iterational_tests)
