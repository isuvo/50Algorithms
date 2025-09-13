"""
Binary heap.

This implementation of a binary heap is a min-heap, which means that the
smallest element is always at the root of the tree. It supports push and pop
operations in O(log n) time.

Time Complexity:
- push: O(log n)
- pop: O(log n)
Space Complexity: O(n), where n is the number of elements in the heap.
"""
from typing import List, TypeVar

T = TypeVar("T")

class BinaryHeap:
    """Simple min-heap with push and pop in O(log n) time."""

    def __init__(self) -> None:
        self.data: List[T] = []

    def push(self, item: T) -> None:
        """Push an item onto the heap."""
        self.data.append(item)
        self._sift_up(len(self.data) - 1)

    def pop(self) -> T:
        """Pop the smallest item from the heap."""
        if not self.data:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        if self.data:
            self._sift_down(0)
        return item

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[idx] < self.data[parent]:
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest != idx:
                self._swap(idx, smallest)
                idx = smallest
            else:
                break

    def _swap(self, i: int, j: int) -> None:
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __len__(self) -> int:
        return len(self.data)

if __name__ == "__main__":
    heap = BinaryHeap[int]()
    heap.push(5)
    heap.push(3)
    heap.push(8)
    heap.push(1)

    print("Heap elements (popped in order):")
    while len(heap) > 0:
        print(heap.pop())