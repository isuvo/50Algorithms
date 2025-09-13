from itertools import combinations

def apriori(transactions, min_support):
    """Find frequent itemsets using the Apriori algorithm.

    Time: exponential in itemset size, Space: O(C)
    """
    transactions = [set(t) for t in transactions]
    items = set().union(*transactions)
    freq = {frozenset([i]): 0 for i in items}
    for t in transactions:
        for i in t:
            freq[frozenset([i])] += 1

    def prune(cand):
        return {k: v for k, v in cand.items() if v >= min_support}

    freq = prune(freq)
    result = dict(freq)
    k = 2
    while freq:
        candidates = {}
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
