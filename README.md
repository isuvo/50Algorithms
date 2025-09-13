# 50Algorithms

This repository provides Python implementations of selected algorithms inspired by *50 Algorithms Every Programmer Should Know*. Each implementation includes a brief explanation and complexity analysis.

## Running the examples

Execute:

```
python run_examples.py
```

to run the sample implementations and see output for the algorithms that are currently implemented.

### Running a single algorithm

The implementations live in the `algorithms/` package and can be invoked
directly from Python.  For example, to run only merge sort:

```bash
python - <<'PY'
from algorithms import merge_sort
print(merge_sort([5, 3, 1]))
PY
```

Any exported function from `algorithms/__init__.py` can be used in the same
way, allowing you to experiment with individual algorithms without executing
the whole demo script.

### Using the accompanying book

A PDF copy of *50 Algorithms Every Programmer Should Know* is included at the
repository root as `Imran A. 50 Algorithms Every Programmer Should Know, 2ed
Python algorithms 2023.pdf`.  Read detailed explanations of each algorithm alongside the code in this
repository.

## Implemented algorithms and complexities

| # | Algorithm | Description | Time complexity | Space complexity |
| - | --------- | ----------- | --------------- | ---------------- |
| 1 | Binary Search | Locate an item in a sorted list via bisection | O(log n) | O(1) |
| 2 | Merge Sort | Divide-and-conquer stable sorting | O(n log n) | O(n) |
| 3 | Quick Sort | Partition-based sorting around a pivot | O(n log n)* | O(log n) |
| 4 | Insertion Sort | Insert each item into sorted prefix | O(n^2) | O(1) |
| 5 | Selection Sort | Repeatedly select minimum element | O(n^2) | O(1) |
| 6 | Bubble Sort | Swap adjacent out-of-order items | O(n^2) | O(1) |
| 7 | Counting Sort | Count occurrences of small integer keys | O(n + k) | O(k) |
| 8 | Radix Sort | Digit-wise sorting using counting sort | O(d*(n + b)) | O(n + b) |
| 9 | Bucket Sort | Distribute and sort into buckets | O(n + k) | O(n) |
| 10 | Heap Sort | Sort via binary heap operations | O(n log n) | O(n) |
| 11 | Shell Sort | Gap-based insertion sort | ~O(n^{3/2}) | O(1) |
| 12 | Quickselect | Select k-th element using partitioning | O(n) avg | O(1) |
| 13 | Breadth-First Search | Layer-by-layer graph traversal | O(V + E) | O(V) |
| 14 | Depth-First Search | Recursive graph traversal | O(V + E) | O(V) |
| 15 | Dijkstra | Shortest paths in weighted graphs | O(E log V) | O(V) |
| 16 | Bellman-Ford | Shortest paths with negative weights | O(V * E) | O(V) |
| 17 | Floyd-Warshall | All-pairs shortest paths | O(V^3) | O(V^2) |
| 18 | Topological Sort | DAG vertex ordering | O(V + E) | O(V) |
| 19 | Kruskal | Minimum spanning tree via edge sorting | O(E log E) | O(V) |
| 20 | Prim | Minimum spanning tree via greedy growth | O(E log V) | O(V) |
| 21 | Union-Find | Disjoint-set union structure | ~O(α(n)) | O(n) |
| 22 | Euclid GCD | Greatest common divisor | O(log n) | O(1) |
| 23 | Sieve of Eratosthenes | Generate primes up to n | O(n log log n) | O(n) |
| 24 | Exponentiation by Squaring | Fast power calculation | O(log n) | O(1) |
| 25 | KMP Search | Linear-time substring search | O(n + m) | O(m) |
| 26 | Rabin-Karp | Rolling-hash substring search | O(n + m) avg | O(1) |
| 27 | Boyer-Moore | Efficient substring search using heuristics | O(n + m) avg | O(m) |
| 28 | Longest Common Subsequence | DP for longest common subsequence | O(n*m) | O(n*m) |
| 29 | Longest Increasing Subsequence | Find longest increasing subsequence | O(n log n) | O(n) |
| 30 | Edit Distance | Levenshtein distance between strings | O(n*m) | O(n*m) |
| 31 | Knapsack DP | 0/1 knapsack via dynamic programming | O(n*W) | O(n*W) |
| 32 | Coin Change DP | Fewest coins for an amount | O(n*amount) | O(amount) |
| 33 | Strassen Matrix Multiply | Fast matrix multiplication | O(n^{log₂7}) | O(n^2) |
| 34 | Huffman Coding | Optimal prefix codes | O(n log n) | O(n) |
| 35 | Fast Fourier Transform | Efficient discrete Fourier transform | O(n log n) | O(n) |
| 36 | Trie | Prefix tree for fast lookups | O(m) | O(total chars) |
| 37 | PageRank | Rank web pages via link analysis | O(iter*(V+E)) | O(V) |
| 38 | Minimax | Game tree search for optimal play | O(b^d) | O(d) |
| 39 | Monte Carlo | Probabilistic simulation algorithm | O(n) | O(1) |
| 40 | Gradient Descent | Optimization via gradient steps | O(iter) | O(1) |
| 41 | Naive Bayes | Probabilistic classifier | O(n*f) | O(f*c) |
| 42 | K-means | Unsupervised clustering | O(iter*n*k) | O(k) |
| 43 | Principal Component Analysis | Dimensionality reduction | O(n*d^2) | O(d^2) |
| 44 | Apriori | Frequent itemset mining | O(n*2^m) | O(2^m) |
| 45 | Simulated Annealing | Stochastic optimization technique | O(iter) | O(1) |
| 46 | A* Search | Heuristic pathfinding | O(E log V) | O(V) |
| 47 | Binary Heap | Priority queue operations | O(log n) | O(n) |
| 48 | In-order Traversal | Binary tree traversal | O(n) | O(n) |
| 49 | Pre-order Traversal | Binary tree traversal | O(n) | O(n) |
| 50 | Post-order Traversal | Binary tree traversal | O(n) | O(n) |

\* Worst case O(n^2)

## Algorithm index

1. `binary_search` – Locate an item in a sorted list by halving the search interval. Run: `python run_examples.py`
2. `merge_sort` – Stable divide-and-conquer sorting by merging sorted halves. Run: `python run_examples.py`
3. `quick_sort` – Partition-based sorting around a pivot. Run: `python run_examples.py`
4. `bfs` – Layer-by-layer graph traversal using a queue. Run: `python run_examples.py`
5. `dfs` – Depth-first graph traversal using recursion or a stack. Run: `python run_examples.py`
6. `dijkstra` – Shortest paths in weighted graphs with non-negative edges. Run: `python run_examples.py`
7. `bellman_ford` – Shortest paths allowing negative edges. Run: `python run_examples.py`
8. `floyd_warshall` – All-pairs shortest paths via dynamic programming. Run: `python run_examples.py`
9. `topological_sort` – Linear ordering of DAG vertices. Run: `python run_examples.py`
10. `kruskal` – Minimum spanning tree via edge sorting. Run: `python run_examples.py`
11. `prim` – Minimum spanning tree using greedy expansion. Run: `python run_examples.py`
12. `a_star` – Heuristic pathfinding. Run: `python run_examples.py`
13. `binary_heap` – Priority queue based on a heap. Run: `python run_examples.py`
14. `counting_sort` – Linear-time sorting for small integer keys. Run: `python run_examples.py`
15. `radix_sort` – Digit-by-digit sorting. Run: `python run_examples.py`
16. `bucket_sort` – Distribution sorting into buckets. Run: `python run_examples.py`
17. `insertion_sort` – In-place iterative insertion. Run: `python run_examples.py`
18. `selection_sort` – In-place selection of minimum elements. Run: `python run_examples.py`
19. `bubble_sort` – Adjacent swaps until sorted. Run: `python run_examples.py`
20. `heap_sort` – Sorting using a binary heap. Run: `python run_examples.py`
21. `shell_sort` – Gap-based generalization of insertion sort. Run: `python run_examples.py`
22. `inorder_traversal` – In-order binary tree traversal. Run: `python run_examples.py`
23. `preorder_traversal` – Pre-order binary tree traversal. Run: `python run_examples.py`
24. `postorder_traversal` – Post-order binary tree traversal. Run: `python run_examples.py`
25. `kmp_search` – Linear-time substring search. Run: `python run_examples.py`
26. `rabin_karp` – Rolling hash based substring search. Run: `python run_examples.py`
27. `boyer_moore` – Efficient substring search using heuristics. Run: `python run_examples.py`
28. `longest_common_subsequence` – DP for longest common subsequence. Run: `python run_examples.py`
29. `longest_increasing_subsequence` – Find longest increasing subsequence. Run: `python run_examples.py`
30. `edit_distance` – Levenshtein distance between strings. Run: `python run_examples.py`
31. `knapsack_dp` – 0/1 knapsack via dynamic programming. Run: `python run_examples.py`
32. `coin_change_dp` – Fewest coins for an amount. Run: `python run_examples.py`
33. `strassen_matrix_multiply` – Fast matrix multiplication. Run: `python run_examples.py`
34. `union_find` – Disjoint set data structure. Run: `python run_examples.py`
35. `quickselect` – Selection algorithm to find k-th element. Run: `python run_examples.py`
36. `huffman_coding` – Optimal prefix codes. Run: `python run_examples.py`
37. `sieve_of_eratosthenes` – Generate prime numbers efficiently. Run: `python run_examples.py`
38. `euclid_gcd` – Compute greatest common divisor. Run: `python run_examples.py`
39. `fast_fourier_transform` – Efficient discrete Fourier transform. Run: `python run_examples.py`
40. `exponentiation_by_squaring` – Fast power calculation. Run: `python run_examples.py`
41. `trie` – Prefix tree for fast lookups. Run: `python run_examples.py`
42. `pagerank` – Rank web pages via link analysis. Run: `python run_examples.py`
43. `minimax` – Game tree search for optimal play. Run: `python run_examples.py`
44. `monte_carlo` – Probabilistic simulation algorithm. Run: `python run_examples.py`
45. `gradient_descent` – Optimization via gradient steps. Run: `python run_examples.py`
46. `naive_bayes` – Probabilistic classifier. Run: `python run_examples.py`
47. `k_means` – Unsupervised clustering. Run: `python run_examples.py`
48. `principal_component_analysis` – Dimensionality reduction. Run: `python run_examples.py`
49. `apriori` – Frequent itemset mining. Run: `python run_examples.py`
50. `simulated_annealing` – Stochastic optimization technique. Run: `python run_examples.py`

## Individual algorithm examples

1. `binary_search`

```bash
python - <<'PY'
from algorithms import binary_search
print(binary_search([1,2,3,4], 3))
PY
```

2. `merge_sort`

```bash
python - <<'PY'
from algorithms import merge_sort
print(merge_sort([5,3,1]))
PY
```

3. `quick_sort`

```bash
python - <<'PY'
from algorithms import quick_sort
print(quick_sort([3,1,4]))
PY
```

4. `bfs`

```bash
python - <<'PY'
from algorithms import bfs
graph={0:[1,2],1:[3],2:[],3:[]}
print(bfs(graph,0))
PY
```

5. `dfs`

```bash
python - <<'PY'
from algorithms import dfs
graph={0:[1,2],1:[3],2:[],3:[]}
print(dfs(graph,0))
PY
```

6. `dijkstra`

```bash
python - <<'PY'
from algorithms import dijkstra
graph={'A':[('B',1),('C',4)],'B':[('C',2)],'C':[]}
print(dijkstra(graph,'A'))
PY
```

7. `bellman_ford`

```bash
python - <<'PY'
from algorithms import bellman_ford
graph={'A':[('B',1)],'B':[('C',2)],'C':[]}
print(bellman_ford(graph,'A'))
PY
```

8. `floyd_warshall`

```bash
python - <<'PY'
from algorithms import floyd_warshall
graph={'A':{'B':3},'B':{'C':4},'C':{}}
print(floyd_warshall(graph))
PY
```

9. `topological_sort`

```bash
python - <<'PY'
from algorithms import topological_sort
graph={'A':['B','C'],'B':['D'],'C':['D'],'D':[]}
print(topological_sort(graph))
PY
```

10. `kruskal`

```bash
python - <<'PY'
from algorithms import kruskal
vertices=[1,2,3]
edges=[(1,2,1),(2,3,2),(1,3,3)]
print(kruskal(vertices,edges))
PY
```

11. `prim`

```bash
python - <<'PY'
from algorithms import prim
graph={1:[(2,1),(3,3)],2:[(3,2)],3:[]}
print(prim(graph,1))
PY
```

12. `a_star`

```bash
python - <<'PY'
from algorithms import a_star
graph={'A':[('B',1),('C',3)],'B':[('C',1)],'C':[]}
heuristic=lambda n:0
print(a_star(graph,'A','C',heuristic))
PY
```

13. `binary_heap`

```bash
python - <<'PY'
from algorithms import BinaryHeap
h=BinaryHeap()
for x in [3,1,4]:
    h.push(x)
print(h.pop())
PY
```

14. `counting_sort`

```bash
python - <<'PY'
from algorithms import counting_sort
print(counting_sort([4,2,2,8,3]))
PY
```

15. `radix_sort`

```bash
python - <<'PY'
from algorithms import radix_sort
print(radix_sort([170,45,75,90]))
PY
```

16. `bucket_sort`

```bash
python - <<'PY'
from algorithms import bucket_sort
print(bucket_sort([0.32,0.25,0.75,0.19]))
PY
```

17. `insertion_sort`

```bash
python - <<'PY'
from algorithms import insertion_sort
print(insertion_sort([3,1,2]))
PY
```

18. `selection_sort`

```bash
python - <<'PY'
from algorithms import selection_sort
print(selection_sort([3,1,2]))
PY
```

19. `bubble_sort`

```bash
python - <<'PY'
from algorithms import bubble_sort
print(bubble_sort([3,1,2]))
PY
```

20. `heap_sort`

```bash
python - <<'PY'
from algorithms import heap_sort
print(heap_sort([3,1,4,1,5]))
PY
```

21. `shell_sort`

```bash
python - <<'PY'
from algorithms import shell_sort
print(shell_sort([3,1,4,1,5]))
PY
```

22. `inorder_traversal`

```bash
python - <<'PY'
from algorithms import inorder
class Node:
    def __init__(self,val,left=None,right=None):
        self.value=val; self.left=left; self.right=right
root=Node(2,Node(1),Node(3))
print(inorder(root))
PY
```

23. `preorder_traversal`

```bash
python - <<'PY'
from algorithms import preorder
class Node:
    def __init__(self,val,left=None,right=None):
        self.value=val; self.left=left; self.right=right
root=Node(2,Node(1),Node(3))
print(preorder(root))
PY
```

24. `postorder_traversal`

```bash
python - <<'PY'
from algorithms import postorder
class Node:
    def __init__(self,val,left=None,right=None):
        self.value=val; self.left=left; self.right=right
root=Node(2,Node(1),Node(3))
print(postorder(root))
PY
```

25. `kmp_search`

```bash
python - <<'PY'
from algorithms import kmp_search
print(kmp_search('ababcabcab','abc'))
PY
```

26. `rabin_karp`

```bash
python - <<'PY'
from algorithms import rabin_karp
print(rabin_karp('ababcabcab','abc'))
PY
```

27. `boyer_moore`

```bash
python - <<'PY'
from algorithms import boyer_moore
print(boyer_moore('abcxabcdabxabcdabcdabcy','abcdabcy'))
PY
```

28. `longest_common_subsequence`

```bash
python - <<'PY'
from algorithms import lcs
print(lcs('ABCBDAB','BDCAB'))
PY
```

29. `longest_increasing_subsequence`

```bash
python - <<'PY'
from algorithms import lis
print(lis([3,1,2,1,8,5,6]))
PY
```

30. `edit_distance`

```bash
python - <<'PY'
from algorithms import edit_distance
print(edit_distance('kitten','sitting'))
PY
```

31. `knapsack_dp`

```bash
python - <<'PY'
from algorithms import knapsack
weights=[2,3,4]; values=[3,4,5]
print(knapsack(weights, values, 5))
PY
```

32. `coin_change_dp`

```bash
python - <<'PY'
from algorithms import coin_change
print(coin_change([1,3,4],6))
PY
```

33. `strassen_matrix_multiply`

```bash
python - <<'PY'
from algorithms import strassen
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
print(strassen(a,b))
PY
```

34. `union_find`

```bash
python - <<'PY'
from algorithms import UnionFind
uf=UnionFind([1,2,3])
uf.union(1,2)
print(uf.find(2))
PY
```

35. `quickselect`

```bash
python - <<'PY'
from algorithms import quickselect
print(quickselect([7,2,1,6,8,5,3,4],2))
PY
```

36. `huffman_coding`

```bash
python - <<'PY'
from algorithms import huffman_encode
print(huffman_encode('banana'))
PY
```

37. `sieve_of_eratosthenes`

```bash
python - <<'PY'
from algorithms import sieve_of_eratosthenes
print(sieve_of_eratosthenes(10))
PY
```

38. `euclid_gcd`

```bash
python - <<'PY'
from algorithms import euclid_gcd
print(euclid_gcd(48,18))
PY
```

39. `fast_fourier_transform`

```bash
python - <<'PY'
from algorithms import fft
print(fft([0,1,0,0]))
PY
```

40. `exponentiation_by_squaring`

```bash
python - <<'PY'
from algorithms import power
print(power(2,10))
PY
```

41. `trie`

```bash
python - <<'PY'
from algorithms import Trie
t=Trie()
t.insert('hi')
print(t.search('hi'))
PY
```

42. `pagerank`

```bash
python - <<'PY'
from algorithms import pagerank
graph={'A':['B'],'B':['C'],'C':['A']}
print(pagerank(graph))
PY
```

43. `minimax`

```bash
python - <<'PY'
from algorithms import MinimaxNode, minimax
tree=MinimaxNode(children=[MinimaxNode(value=3), MinimaxNode(children=[MinimaxNode(value=2), MinimaxNode(value=5)])])
print(minimax(tree, True))
PY
```

44. `monte_carlo`

```bash
python - <<'PY'
from algorithms import monte_carlo_pi
print(monte_carlo_pi(1000))
PY
```

45. `gradient_descent`

```bash
python - <<'PY'
from algorithms import gradient_descent
f=lambda x:(x-3)**2
df=lambda x:2*(x-3)
print(gradient_descent(f, df, 0)[0])
PY
```

46. `naive_bayes`

```bash
python - <<'PY'
from algorithms import NaiveBayes
X=[{'weather':'sunny'},{'weather':'rainy'}]
y=['dry','wet']
model=NaiveBayes()
model.fit(X,y)
print(model.predict({'weather':'rainy'}))
PY
```

47. `k_means`

```bash
python - <<'PY'
from algorithms import k_means
points=[(0,0),(1,1),(5,5)]
print(k_means(points,2))
PY
```

48. `principal_component_analysis`

```bash
python - <<'PY'
from algorithms import pca
points=[(1,2),(2,3),(3,4)]
print(pca(points))
PY
```

49. `apriori`

```bash
python - <<'PY'
from algorithms import apriori
transactions=[[1,2],[1,2,3],[1,3]]
print(apriori(transactions,2))
PY
```

50. `simulated_annealing`

```bash
python - <<'PY'
from algorithms import simulated_annealing
f=lambda x:(x-2)**2
print(simulated_annealing(f,0)[0])
PY


