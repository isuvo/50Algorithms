from heapq import heappush, heappop, heapify


class _Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encode(data):
    """Generate Huffman codes for given data string.

    Time: O(n log n), Space: O(n)
    """
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

    def build(node, prefix=""):
        if node.char is not None:
            codes[node.char] = prefix
        else:
            build(node.left, prefix + "0")
            build(node.right, prefix + "1")

    build(root)
    return codes
