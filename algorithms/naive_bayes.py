"""Simple multinomial Naive Bayes for categorical features.

Training time: O(n*f), where n is the number of training examples and f is the
number of features.
Prediction time: O(c*f), where c is the number of classes and f is the number
of features.
Space: O(c*f*v), where c is the number of classes, f is the number of features,
and v is the number of unique values for each feature.
"""

from collections import defaultdict, Counter
from typing import List, Dict, Any, Hashable

class NaiveBayes:
    """Simple multinomial Naive Bayes for categorical features."""

    def fit(self, X: List[Dict[Hashable, Any]], y: List[Hashable]) -> None:
        """Fit the Naive Bayes model to the training data."""
        self.classes = set(y)
        self.class_counts = Counter(y)
        self.feature_counts: Dict[Hashable, Dict[Hashable, Counter]] = {c: defaultdict(Counter) for c in self.classes}
        for features, label in zip(X, y):
            for f, v in features.items():
                self.feature_counts[label][f][v] += 1
        self.total = len(y)

    def predict(self, features: Dict[Hashable, Any]) -> Hashable:
        """Predict the class label for a given set of features."""
        best, best_prob = None, -1
        for c in self.classes:
            prob = self.class_counts[c] / self.total
            for f, v in features.items():
                # Add-1 smoothing
                prob *= (self.feature_counts[c][f][v] + 1) / (
                    self.class_counts[c] + len(self.feature_counts[c][f])
                )
            if prob > best_prob:
                best, best_prob = c, prob
        return best

if __name__ == "__main__":
    # Example: Spam classification
    X_train = [
        {'word1': 1, 'word2': 0, 'word3': 1},
        {'word1': 0, 'word2': 1, 'word3': 1},
        {'word1': 1, 'word2': 1, 'word3': 0},
        {'word1': 0, 'word2': 0, 'word3': 1},
    ]
    y_train = ['spam', 'ham', 'spam', 'ham']

    model = NaiveBayes()
    model.fit(X_train, y_train)

    X_test = {'word1': 1, 'word2': 0, 'word3': 1}
    prediction = model.predict(X_test)
    print(f"The prediction for {X_test} is: {prediction}")