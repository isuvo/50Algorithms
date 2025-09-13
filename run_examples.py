"""Run sample executions of the algorithms and print the results."""
from algorithms import (
    binary_search,
    merge_sort,
    quick_sort,
    insertion_sort,
    selection_sort,
    bubble_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
    shell_sort,
    quickselect,
    bfs,
    dfs,
    dijkstra,
    bellman_ford,
    floyd_warshall,
    topological_sort,
    kruskal,
    prim,
    euclid_gcd,
    sieve_of_eratosthenes,
    power,
    kmp_search,
    rabin_karp,
)

# Sorting examples
unsorted_list = [5, 3, 8, 4, 2]
print("merge_sort:", merge_sort(unsorted_list))
print("quick_sort:", quick_sort(unsorted_list))
print("insertion_sort:", insertion_sort(unsorted_list))
print("selection_sort:", selection_sort(unsorted_list))
print("bubble_sort:", bubble_sort(unsorted_list))
print("heap_sort:", heap_sort(unsorted_list))
print("shell_sort:", shell_sort(unsorted_list))

int_list = [5, 3, 0, 2, 3, 1]
print("counting_sort:", counting_sort(int_list))
print("radix_sort:", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
print("bucket_sort:", bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))

print("quickselect k=2:", quickselect(unsorted_list, 2))

# Binary search example
sorted_list = [1, 3, 4, 5, 7, 8]
print("binary_search for 5:", binary_search(sorted_list, 5))
print("binary_search for 6:", binary_search(sorted_list, 6))

# Graph examples
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("bfs:", bfs(graph, 'A'))
print("dfs:", dfs(graph, 'A'))

weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print("dijkstra:", dijkstra(weighted_graph, 'A'))

# Bellman-Ford example
bf_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', -1), ('D', 2)],
    'C': [('D', 3)],
    'D': []
}
print("bellman_ford:", bellman_ford(bf_graph, 'A'))

# Floyd-Warshall example
fw_graph = {
    'A': {'B': 5, 'C': 9, 'D': 1},
    'B': {'C': 2},
    'C': {'D': 7},
    'D': {'B': 2, 'C': 6}
}
print("floyd_warshall:", floyd_warshall(fw_graph))

# Topological sort example
dag = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
print("topological_sort:", topological_sort(dag))

# Minimum spanning tree examples
mst_vertices = ['A', 'B', 'C', 'D']
mst_edges = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 2), ('C', 'D', 1)]
print("kruskal:", kruskal(mst_vertices, mst_edges))
prim_graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('C', 2), ('D', 3)],
    'C': [('D', 1)],
    'D': []
}
print("prim:", prim(prim_graph, 'A'))

# Number theory and string algorithms
print("euclid_gcd:", euclid_gcd(48, 18))
print("sieve_of_eratosthenes:", sieve_of_eratosthenes(20))
print("power 2^10:", power(2, 10))
text = "ababcabcabababd"
pattern = "ababd"
print("kmp_search:", kmp_search(text, pattern))
print("rabin_karp:", rabin_karp(text, pattern))
