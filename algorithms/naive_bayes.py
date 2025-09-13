from collections import defaultdict, Counter


class NaiveBayes:
    """Simple multinomial Naive Bayes for categorical features.

    Training time: O(n*f), Space: O(f*c)
    """

    def fit(self, X, y):
        self.classes = set(y)
        self.class_counts = Counter(y)
        self.feature_counts = {c: defaultdict(Counter) for c in self.classes}
        for features, label in zip(X, y):
            for f, v in features.items():
                self.feature_counts[label][f][v] += 1
        self.total = len(y)

    def predict(self, features):
        best, best_prob = None, -1
        for c in self.classes:
            prob = self.class_counts[c] / self.total
            for f, v in features.items():
                prob *= (self.feature_counts[c][f][v] + 1) / (
                    self.class_counts[c] + len(self.feature_counts[c][f])
                )
            if prob > best_prob:
                best, best_prob = c, prob
        return best
