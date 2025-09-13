"""
Apriori algorithm for frequent itemset mining.

This implementation of the Apriori algorithm finds frequent itemsets in a
dataset of transactions. The algorithm works by iteratively generating
candidate itemsets of a certain size and then pruning the candidates that do
not meet the minimum support threshold.

Time Complexity: O(2^m), where m is the number of items in the largest itemset.
Space Complexity: O(C), where C is the number of candidate itemsets.
"""
from itertools import combinations
from typing import List, Set, Dict, FrozenSet

Item = str
Transaction = Set[Item]
Itemset = FrozenSet[Item]

def apriori(transactions: List[Transaction], min_support: int) -> Dict[Itemset, int]:
    """
    Find frequent itemsets using the Apriori algorithm.

    Args:
        transactions: A list of transactions, where each transaction is a set of items.
        min_support: The minimum support threshold for an itemset to be considered frequent.

    Returns:
        A dictionary mapping frequent itemsets to their support counts.
    """
    transactions = [set(t) for t in transactions]
    items = set().union(*transactions)
    freq = {frozenset([i]): 0 for i in items}
    for t in transactions:
        for i in t:
            freq[frozenset([i])] += 1

    def prune(cand: Dict[Itemset, int]) -> Dict[Itemset, int]:
        return {k: v for k, v in cand.items() if v >= min_support}

    freq = prune(freq)
    result = dict(freq)
    k = 2
    while freq:
        candidates: Dict[Itemset, int] = {}
        sets = list(freq.keys())
        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                union = sets[i] | sets[j]
                if len(union) == k:
                    candidates[union] = 0
        for t in transactions:
            for cand in candidates:
                if cand.issubset(t):
                    candidates[cand] += 1
        freq = prune(candidates)
        result.update(freq)
        k += 1
    return result

if __name__ == "__main__":
    transactions = [
        {'bread', 'milk'},
        {'bread', 'diapers', 'beer', 'eggs'},
        {'milk', 'diapers', 'beer', 'cola'},
        {'bread', 'milk', 'diapers', 'beer'},
        {'bread', 'milk', 'diapers', 'cola'},
    ]
    min_support = 3
    frequent_itemsets = apriori(transactions, min_support)
    print(f"Frequent itemsets with minimum support {min_support}:")
    for itemset, support in frequent_itemsets.items():
        print(f"- {list(itemset)}: {support}")