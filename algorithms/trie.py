class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    """Prefix tree supporting insertion and exact search.

    Insert/Search time: O(m) for word length m. Space: O(total chars)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end
