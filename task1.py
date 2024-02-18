""" 
Task 1.
- Implement depth-first search
- Test depth-first search path 1 => 9
- Test depth-first search with various starting and ending positions
"""

from graph import GRAPH
from test import test, compare_tests, random_node, display

# Recursive approach
def dfs_recurse(graph, start, end, visited):
    if start in visited:
        return
    visited.append(start)

    if start is end:
        return visited

    siblings = graph[start]
    for sibling in siblings:
        found_path = dfs_recurse(graph, sibling, end, visited)
        if found_path:
            return found_path

# Iterative stack approach
def dfs_stack(graph, start, end, visited):
    stack = [start]
    while stack:
        root = stack.pop()
        if root in visited:
            continue

        visited.append(root)

        if root is end:
            return visited

        siblings = graph[root]
        stack.extend(siblings)

if __name__ == "__main__":
    # Test DFS 1 => 9
    test1 = display(test(dfs_stack, GRAPH, 1, 9))
    test2 = display(test(dfs_recurse, GRAPH, 1, 9))
    compare_tests('1=>9 dfs stack vs recurse', test1, test2)

    # Test all combinations
    recurse_tests = []
    stack_tests = []

    for start in GRAPH.keys():
        for end in GRAPH.keys():
            recurse_tests.append(test(dfs_recurse, GRAPH, start, end))
            stack_tests.append(test(dfs_stack, GRAPH, start, end))

    compare_tests('all dfs combinations recurse', *recurse_tests)
    compare_tests('all dfs combinations stack', *stack_tests)
    compare_tests('all dfs combinations recurse vs stack', *recurse_tests, *stack_tests)

    # Test random paths
    recurse_tests = []
    stack_tests = []

    for _ in range(10000):
        start = random_node(GRAPH)
        end = random_node(GRAPH)

        recurse_tests.append(test(dfs_recurse, GRAPH, start, end))
        stack_tests.append(test(dfs_stack, GRAPH, start, end))

    compare_tests('random dfs recurse', *recurse_tests)
    compare_tests('random dfs stack', *stack_tests)
    compare_tests('random dfs recurse vs stack', *recurse_tests, *stack_tests)
