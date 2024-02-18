"""
Testing of search algorithms
Provides methods for:
- Measuring space and time of an algorithm
- Comparing multiple test cases
- Selecting random input for testing
"""

from collections import namedtuple
from time import perf_counter
from datetime import timedelta
from random import choice

TestResult = namedtuple('TestResult', 'search_algo graph start end path visited coverage t_elapsed')

def _fmt_path(test_result):
    return ' => '.join(map(str, test_result.path)) if test_result.path else 'Not found'

def _fmt_visited(test_result):
    graph_nodes = len(test_result.graph)
    coverage_percent = test_result.coverage * 100
    visited_str = f'{test_result.visited} / {graph_nodes} nodes ({coverage_percent:.1f}%)'

    return visited_str

def _fmt_elapsed(test_result):
    return timedelta(seconds=test_result.t_elapsed)

def test(search_algo, graph, start, end):
    t_start = perf_counter()
    path = search_algo(graph, start, end, [])
    t_end = perf_counter()
    t_elapsed = t_end - t_start
    
    graph_nodes = len(graph)
    visited = len(path) if path else 0
    coverage = visited / graph_nodes

    return TestResult(search_algo, graph, start, end, path, visited, coverage, t_elapsed)

def display(test_result):
    algo_name = test_result.search_algo.__name__
    path_str = _fmt_path(test_result)
    visited_str = _fmt_visited(test_result)
    elapsed_str = _fmt_elapsed(test_result)

    print(f"{algo_name}: {test_result.start} => {test_result.end}:")
    print('Path:', path_str)
    print('Visited:', visited_str)
    print('Elapsed time:', elapsed_str)
    print()
    return test_result

def compare_tests(comparison_name, *args):
    valid_tests = [x for x in args if x.path is not None]
    failed_tests_amount = len(args) - len(valid_tests)

    print('----------------------------')
    print(f'Comparison {comparison_name} results:')
    print('Total test cases:', len(valid_tests))
    print()

    if valid_tests:
        shortest_path = min(valid_tests, key=lambda x: len(x.path))
        longest_path = max(valid_tests, key=lambda x: len(x.path))

        average_coverage = sum(map(lambda x: x.coverage, valid_tests)) / len(valid_tests)

        fastest_search = min(valid_tests, key=lambda x: x.t_elapsed)
        slowest_search = max(valid_tests, key=lambda x: x.t_elapsed)

        total_search = sum(map(lambda x: x.t_elapsed, valid_tests)) 
        average_search = total_search / len(valid_tests)

        print(f'Shortest path: {shortest_path.search_algo.__name__}: {shortest_path.start} => {shortest_path.end}')
        print('Path:', _fmt_path(shortest_path))
        print('Visited:', _fmt_visited(shortest_path))
        print()

        print(f'Longest path: {longest_path.search_algo.__name__}: {longest_path.start} => {longest_path.end}')
        print('Path:', _fmt_path(longest_path))
        print('Visited:', _fmt_visited(longest_path))
        print()

        print(f'Fastest search: {fastest_search.search_algo.__name__}: {fastest_search.start} => {fastest_search.end}')
        print('Elapsed time:', _fmt_elapsed(fastest_search))
        print()

        print(f'Slowest search: {slowest_search.search_algo.__name__}: {slowest_search.start} => {slowest_search.end}')
        print('Elapsed time:', _fmt_elapsed(slowest_search))
        print()

        print(f'Average coverage: {average_coverage * 100:.1f}%')
        print(f'Average search time:', timedelta(seconds=average_search))
        print(f'Total search time:', timedelta(seconds=total_search))

        if failed_tests_amount > 0:
            print()
            print('Failed tests amount:', failed_tests_amount)

    print('----------------------------')
    print()

def random_node(graph):
    return choice(list(graph.keys()))

