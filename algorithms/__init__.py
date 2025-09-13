"""Collection of classic algorithms with descriptive docstrings."""

from .binary_search import binary_search
from .merge_sort import merge_sort
from .quick_sort import quick_sort
from .insertion_sort import insertion_sort
from .selection_sort import selection_sort
from .bubble_sort import bubble_sort
from .counting_sort import counting_sort
from .radix_sort import radix_sort
from .bucket_sort import bucket_sort
from .heap_sort import heap_sort
from .shell_sort import shell_sort
from .quickselect import quickselect
from .bfs import bfs
from .dfs import dfs
from .dijkstra import dijkstra
from .bellman_ford import bellman_ford
from .floyd_warshall import floyd_warshall
from .topological_sort import topological_sort
from .union_find import UnionFind
from .kruskal import kruskal
from .prim import prim
from .euclid_gcd import euclid_gcd
from .sieve_of_eratosthenes import sieve_of_eratosthenes
from .exponentiation_by_squaring import power
from .kmp_search import kmp_search
from .rabin_karp import rabin_karp
from .a_star import a_star
from .binary_heap import BinaryHeap
from .inorder_traversal import inorder
from .preorder_traversal import preorder
from .postorder_traversal import postorder
from .boyer_moore import boyer_moore
from .longest_common_subsequence import lcs
from .longest_increasing_subsequence import lis
from .edit_distance import edit_distance
from .knapsack_dp import knapsack
from .coin_change_dp import coin_change
from .strassen_matrix_multiply import strassen
from .huffman_coding import huffman_encode
from .fast_fourier_transform import fft
from .trie import Trie
from .pagerank import pagerank
from .minimax import Node as MinimaxNode, minimax
from .monte_carlo import monte_carlo_pi
from .gradient_descent import gradient_descent
from .naive_bayes import NaiveBayes
from .k_means import k_means
from .principal_component_analysis import pca
from .apriori import apriori
from .simulated_annealing import simulated_annealing

__all__ = [
    "binary_search",
    "merge_sort",
    "quick_sort",
    "insertion_sort",
    "selection_sort",
    "bubble_sort",
    "counting_sort",
    "radix_sort",
    "bucket_sort",
    "heap_sort",
    "shell_sort",
    "quickselect",
    "bfs",
    "dfs",
    "dijkstra",
    "bellman_ford",
    "floyd_warshall",
    "topological_sort",
    "UnionFind",
    "kruskal",
    "prim",
    "euclid_gcd",
    "sieve_of_eratosthenes",
    "power",
    "kmp_search",
    "rabin_karp",
    "a_star",
    "BinaryHeap",
    "inorder",
    "preorder",
    "postorder",
    "boyer_moore",
    "lcs",
    "lis",
    "edit_distance",
    "knapsack",
    "coin_change",
    "strassen",
    "huffman_encode",
    "fft",
    "Trie",
    "pagerank",
    "MinimaxNode",
    "minimax",
    "monte_carlo_pi",
    "gradient_descent",
    "NaiveBayes",
    "k_means",
    "pca",
    "apriori",
    "simulated_annealing",
]
