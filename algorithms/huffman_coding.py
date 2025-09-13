"""
Huffman coding for data compression.

This implementation of Huffman coding generates a prefix-free binary code for a
given set of characters. The algorithm works by building a binary tree from the
bottom up, where the leaves represent the characters and their frequencies, and
the internal nodes represent the sum of the frequencies of their children. The
binary code for each character is then obtained by traversing the tree from the
root to the leaf corresponding to the character.

Time Complexity: O(n log n), where n is the number of unique characters in the
input data.
Space Complexity: O(n), where n is the number of unique characters in the
input data.
"""
from heapq import heappush, heappop, heapify
from typing import Dict, Optional

class _Node:
    """A node in the Huffman tree."""
    def __init__(self, char: Optional[str] = None, freq: int = 0, left: Optional["_Node"] = None, right: Optional["_Node"] = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other: "_Node") -> bool:
        return self.freq < other.freq

def huffman_encode(data: str) -> Dict[str, str]:
    """
    Generate Huffman codes for a given data string.

    Args:
        data: The input data string.

    Returns:
        A dictionary mapping each character to its Huffman code.
    """
    if not data:
        return {}
    freq = {}
    for ch in data:
        freq[ch] = freq.get(ch, 0) + 1
    heap = [_Node(ch, f) for ch, f in freq.items()]
    heapify(heap)
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, _Node(None, a.freq + b.freq, a, b))
    root = heap[0]
    codes = {}

    def build(node: _Node, prefix: str = "") -> None:
        if node.char is not None:
            codes[node.char] = prefix
        else:
            build(node.left, prefix + "0")
            build(node.right, prefix + "1")

    build(root)
    return codes

if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    codes = huffman_encode(data)
    print("Huffman codes:")
    for char, code in sorted(codes.items()):
        print(f"- '{char}': {code}")