# 50Algorithms

This repository provides Python implementations of selected algorithms inspired by *50 Algorithms Every Programmer Should Know*. Each implementation includes a brief explanation and complexity analysis.

## Running the examples

Execute:

```
python run_examples.py
```

to run the sample implementations and see output for the algorithms that are currently implemented.

## Implemented algorithms and complexities

| # | Algorithm       | Description                                   | Time complexity | Space complexity |
| - | --------------- | --------------------------------------------- | --------------- | ---------------- |
| 1 | Binary Search   | Locate an item in a sorted list via bisection | O(log n)        | O(1)             |
| 2 | Merge Sort      | Divide-and-conquer stable sorting             | O(n log n)      | O(n)             |
| 3 | Quick Sort      | Partition-based sorting around a pivot        | O(n log n)*     | O(log n)         |
| 4 | Insertion Sort  | Insert each item into sorted prefix          | O(n^2)          | O(1)             |
| 5 | Selection Sort  | Repeatedly select minimum element            | O(n^2)          | O(1)             |
| 6 | Bubble Sort     | Swap adjacent out-of-order items             | O(n^2)          | O(1)             |
| 7 | Counting Sort   | Count occurrences of small integer keys      | O(n + k)        | O(k)             |
| 8 | Radix Sort      | Digit-wise sorting using counting sort       | O(d*(n + b))    | O(n + b)         |
| 9 | Bucket Sort     | Distribute and sort into buckets             | O(n + k)        | O(n)             |
| 10 | Heap Sort       | Sort via binary heap operations              | O(n log n)      | O(n)             |
| 11 | Shell Sort      | Gap-based insertion sort                     | ~O(n^{3/2})     | O(1)             |
| 12 | Quickselect     | Select k-th element using partitioning       | O(n) avg        | O(1)             |
| 13 | Breadth-First Search | Layer-by-layer graph traversal          | O(V + E)        | O(V)             |
| 14 | Depth-First Search  | Recursive graph traversal                | O(V + E)        | O(V)             |
| 15 | Dijkstra            | Shortest paths in weighted graphs        | O(E log V)      | O(V)             |
| 16 | Bellman-Ford        | Shortest paths with negative weights     | O(V * E)        | O(V)             |
| 17 | Floyd-Warshall      | All-pairs shortest paths                 | O(V^3)          | O(V^2)           |
| 18 | Topological Sort    | DAG vertex ordering                      | O(V + E)        | O(V)             |
| 19 | Kruskal             | Minimum spanning tree via edge sorting   | O(E log E)      | O(V)             |
| 20 | Prim                | Minimum spanning tree via greedy growth  | O(E log V)      | O(V)             |
| 21 | Union-Find          | Disjoint-set union structure             | ~O(α(n))        | O(n)             |
| 22 | Euclid GCD          | Greatest common divisor                  | O(log n)        | O(1)             |
| 23 | Sieve of Eratosthenes | Generate primes up to n               | O(n log log n)  | O(n)             |
| 24 | Exponentiation by Squaring | Fast power calculation           | O(log n)        | O(1)             |
| 25 | KMP Search          | Linear-time substring search             | O(n + m)        | O(m)             |
| 26 | Rabin-Karp          | Rolling-hash substring search            | O(n + m) avg    | O(1)             |

\* Worst case O(n^2)

## Algorithm index

1. `binary_search_1` – Locate an item in a sorted list by halving the search interval. Run: `python run_examples.py`
2. `merge_sort_2` – Stable divide-and-conquer sorting by merging sorted halves. Run: `python run_examples.py`
3. `quick_sort_3` – Partition-based sorting around a pivot. Run: `python run_examples.py`
4. `bfs_4` – Layer-by-layer graph traversal using a queue. Run: `python run_examples.py`
5. `dfs_5` – Depth-first graph traversal using recursion or a stack. Run: `python run_examples.py`
6. `dijkstra_6` – Shortest paths in weighted graphs with non-negative edges. Run: `python run_examples.py`
7. `bellman_ford_7` – Shortest paths allowing negative edges. Run: `python run_examples.py`
8. `floyd_warshall_8` – All-pairs shortest paths via dynamic programming. Run: `python run_examples.py`
9. `topological_sort_9` – Linear ordering of DAG vertices. Run: `python run_examples.py`
10. `kruskal_10` – Minimum spanning tree via edge sorting. Run: `python run_examples.py`
11. `prim_11` – Minimum spanning tree using greedy expansion. Run: `python run_examples.py`
12. `a_star_12` – Heuristic pathfinding. *Implementation pending*
13. `binary_heap_13` – Priority queue based on a heap. *Implementation pending*
14. `counting_sort_14` – Linear-time sorting for small integer keys. Run: `python run_examples.py`
15. `radix_sort_15` – Digit-by-digit sorting. Run: `python run_examples.py`
16. `bucket_sort_16` – Distribution sorting into buckets. Run: `python run_examples.py`
17. `insertion_sort_17` – In-place iterative insertion. Run: `python run_examples.py`
18. `selection_sort_18` – In-place selection of minimum elements. Run: `python run_examples.py`
19. `bubble_sort_19` – Adjacent swaps until sorted. Run: `python run_examples.py`
20. `heap_sort_20` – Sorting using a binary heap. Run: `python run_examples.py`
21. `shell_sort_21` – Gap-based generalization of insertion sort. Run: `python run_examples.py`
22. `inorder_traversal_22` – In-order binary tree traversal. *Implementation pending*
23. `preorder_traversal_23` – Pre-order binary tree traversal. *Implementation pending*
24. `postorder_traversal_24` – Post-order binary tree traversal. *Implementation pending*
25. `kmp_search_25` – Linear-time substring search. Run: `python run_examples.py`
26. `rabin_karp_26` – Rolling hash based substring search. Run: `python run_examples.py`
27. `boyer_moore_27` – Efficient substring search using heuristics. *Implementation pending*
28. `longest_common_subsequence_28` – DP for longest common subsequence. *Implementation pending*
29. `longest_increasing_subsequence_29` – Find longest increasing subsequence. *Implementation pending*
30. `edit_distance_30` – Levenshtein distance between strings. *Implementation pending*
31. `knapsack_dp_31` – 0/1 knapsack via dynamic programming. *Implementation pending*
32. `coin_change_dp_32` – Fewest coins for an amount. *Implementation pending*
33. `strassen_matrix_multiply_33` – Fast matrix multiplication. *Implementation pending*
34. `union_find_34` – Disjoint set data structure. Run: `python run_examples.py`
35. `quickselect_35` – Selection algorithm to find k-th element. Run: `python run_examples.py`
36. `huffman_coding_36` – Optimal prefix codes. *Implementation pending*
37. `sieve_of_eratosthenes_37` – Generate prime numbers efficiently. Run: `python run_examples.py`
38. `euclid_gcd_38` – Compute greatest common divisor. Run: `python run_examples.py`
39. `fast_fourier_transform_39` – Efficient discrete Fourier transform. *Implementation pending*
40. `exponentiation_by_squaring_40` – Fast power calculation. Run: `python run_examples.py`
41. `trie_41` – Prefix tree for fast lookups. *Implementation pending*
42. `pagerank_42` – Rank web pages via link analysis. *Implementation pending*
43. `minimax_43` – Game tree search for optimal play. *Implementation pending*
44. `monte_carlo_44` – Probabilistic simulation algorithm. *Implementation pending*
45. `gradient_descent_45` – Optimization via gradient steps. *Implementation pending*
46. `naive_bayes_46` – Probabilistic classifier. *Implementation pending*
47. `k_means_47` – Unsupervised clustering. *Implementation pending*
48. `principal_component_analysis_48` – Dimensionality reduction. *Implementation pending*
49. `apriori_49` – Frequent itemset mining. *Implementation pending*
50. `simulated_annealing_50` – Stochastic optimization technique. *Implementation pending*

