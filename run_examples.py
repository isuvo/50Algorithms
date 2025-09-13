from dataclasses import dataclass



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
    UnionFind,
    kruskal,
    prim,
    euclid_gcd,
    sieve_of_eratosthenes,
    power,
    kmp_search,
    rabin_karp,
    a_star,
    BinaryHeap,
    inorder,
    preorder,
    postorder,
    boyer_moore,
    lcs,
    lis,
    edit_distance,
    knapsack,
    coin_change,
    strassen,
    huffman_encode,
    fft,
    Trie,
    pagerank,
    MinimaxNode,
    minimax,
    monte_carlo_pi,
    gradient_descent,
    NaiveBayes,
    k_means,
    pca,
    apriori,
    simulated_annealing,
)


def demo_sorting() -> None:
    """Showcase sorting and selection algorithms."""

    print("=== Sorting and selection ===")
    data = [5, 3, 8, 4, 2]
    print("merge_sort:", merge_sort(data))
    print("quick_sort:", quick_sort(data))
    print("insertion_sort:", insertion_sort(data))
    print("selection_sort:", selection_sort(data))
    print("bubble_sort:", bubble_sort(data))
    print("heap_sort:", heap_sort(data))
    print("shell_sort:", shell_sort(data))
    print("counting_sort:", counting_sort([5, 3, 0, 2, 3, 1]))
    print("radix_sort:", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
    print(
        "bucket_sort:",
        bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]),
    )
    print("quickselect k=2:", quickselect(data, 2))
    sorted_list = [1, 3, 4, 5, 7, 8]
    print("binary_search 5:", binary_search(sorted_list, 5))
    print("binary_search missing 6:", binary_search(sorted_list, 6))


def demo_graph() -> None:
    """Run graph algorithm demonstrations."""

    print("\n=== Graph algorithms ===")
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    print("bfs:", bfs(graph, "A"))
    print("dfs:", dfs(graph, "A"))

    wgraph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    print("dijkstra:", dijkstra(wgraph, "A"))

    bf = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", -1), ("D", 2)],
        "C": [("D", 3)],
        "D": [],
    }
    print("bellman_ford:", bellman_ford(bf, "A"))

    fw = {
        "A": {"B": 5, "C": 9, "D": 1},
        "B": {"C": 2},
        "C": {"D": 7},
        "D": {"B": 2, "C": 6},
    }
    print("floyd_warshall:", floyd_warshall(fw))

    dag = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    print("topological_sort:", topological_sort(dag))

    vertices = ["A", "B", "C", "D"]
    edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 2), ("C", "D", 1)]
    print("kruskal:", kruskal(vertices, edges))

    prim_graph = {
        "A": [("B", 1), ("C", 2)],
        "B": [("C", 2), ("D", 3)],
        "C": [("D", 1)],
        "D": [],
    }
    print("prim:", prim(prim_graph, "A"))

    astar_graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    h = lambda n: {"A": 3, "B": 2, "C": 1, "D": 0}[n]
    print("a_star:", a_star(astar_graph, "A", "D", h))

    uf = UnionFind([1, 2, 3, 4])
    uf.union(1, 2)
    uf.union(3, 4)
    print("union_find connected 1&2:", uf.find(1) == uf.find(2))


def demo_structures() -> None:
    """Illustrate basic data structures and tree traversals."""

    print("\n=== Data structures and traversals ===")
    heap = BinaryHeap()
    for x in [5, 3, 8]:
        heap.push(x)
    print("binary_heap pops:", [heap.pop() for _ in range(3)])

    @dataclass
    class Node:
        value: int
        left: "Node | None" = None
        right: "Node | None" = None

    tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    print("inorder:", inorder(tree))
    print("preorder:", preorder(tree))
    print("postorder:", postorder(tree))

    trie = Trie()
    trie.insert("hello")
    print("trie search 'hello':", trie.search("hello"))
    print("trie search 'bye':", trie.search("bye"))


def demo_strings_dp() -> None:
    """Demonstrate string searching and dynamic programming algorithms."""

    print("\n=== Strings and dynamic programming ===")
    text = "ababcabcabababd"
    pattern = "ababd"
    print("kmp_search:", kmp_search(text, pattern))
    print("rabin_karp:", rabin_karp(text, pattern))
    print("boyer_moore:", boyer_moore(text, pattern))
    print("lcs:", lcs("ABCBDAB", "BDCABA"))
    print("lis:", lis([3, 4, -1, 0, 6, 2, 3]))
    print("edit_distance:", edit_distance("kitten", "sitting"))
    print("knapsack:", knapsack([2, 3, 4], [4, 5, 6], 5))
    print("coin_change:", coin_change([1, 2, 5], 11))


def demo_misc() -> None:
    """Show miscellaneous math and machine-learning routines."""

    print("\n=== Math, AI, and other algorithms ===")
    print("euclid_gcd:", euclid_gcd(48, 18))
    print("sieve_of_eratosthenes:", sieve_of_eratosthenes(20))
    print("power 2^10:", power(2, 10))
    print("strassen:", strassen([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print("huffman_encode:", huffman_encode('beep boop beer'))
    print("fft:", fft([0, 1, 0, -1]))
    print("pagerank:", pagerank({"A": ["B", "C"], "B": ["C"], "C": ["A"]}, iterations=10))

    root = MinimaxNode(
        children=[
            MinimaxNode(children=[MinimaxNode(value=3), MinimaxNode(value=5)]),
            MinimaxNode(children=[MinimaxNode(value=2), MinimaxNode(value=9)]),
        ]
    )
    print("minimax:", minimax(root, True))

    print("monte_carlo_pi:", monte_carlo_pi(1000))

    f = lambda x: x * x
    df = lambda x: 2 * x
    print("gradient_descent:", gradient_descent(f, df, 10, 0.1, 100))

    nb = NaiveBayes()
    X = [
        {"weather": "sunny"},
        {"weather": "rainy"},
        {"weather": "sunny"},
        {"weather": "sunny"},
    ]
    y = ["play", "stay", "play", "play"]
    nb.fit(X, y)
    print("naive_bayes:", nb.predict({"weather": "rainy"}))

    points = [(1, 1), (1.5, 2), (3, 4), (5, 7)]
    print("k_means:", k_means(points, 2))

    pca_pts = [(2.5, 2.4), (0.5, 0.7), (2.2, 2.9), (1.9, 2.2)]
    print("pca:", pca(pca_pts))

    transactions = [
        ["milk", "bread"],
        ["bread", "diaper", "beer"],
        ["milk", "diaper", "bread", "beer"],
        ["bread"],
    ]
    print("apriori:", apriori(transactions, 2))

    print("simulated_annealing:", simulated_annealing(f, 10, 1.0, 0.9, 100))


if __name__ == "__main__":
    demo_sorting()
    demo_graph()
    demo_structures()
    demo_strings_dp()
    demo_misc()
