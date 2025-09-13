"""
K-means clustering algorithm.

This implementation of the k-means algorithm partitions a set of 2D points into
k clusters. The algorithm iteratively assigns each point to the nearest
centroid and then recalculates the centroids as the mean of the points in each
cluster.

Time Complexity: O(i * n * k), where i is the number of iterations, n is the
number of points, and k is the number of clusters.
Space Complexity: O(n + k)
"""
import random
from typing import List, Tuple

Point = Tuple[float, float]

def k_means(points: List[Point], k: int, iterations: int = 10) -> List[Point]:
    """
    Cluster 2D points into k groups using the k-means algorithm.

    Args:
        points: A list of 2D points to cluster.
        k: The number of clusters to create.
        iterations: The number of iterations to run the algorithm.

    Returns:
        A list of k centroids representing the centers of the clusters.
    """
    centroids = random.sample(points, k)
    for _ in range(iterations):
        clusters = {i: [] for i in range(k)}
        for p in points:
            idx = min(range(k), key=lambda i: (p[0] - centroids[i][0]) ** 2 + (p[1] - centroids[i][1]) ** 2)
            clusters[idx].append(p)
        for i in range(k):
            if clusters[i]:
                x = sum(p[0] for p in clusters[i]) / len(clusters[i])
                y = sum(p[1] for p in clusters[i]) / len(clusters[i])
                centroids[i] = (x, y)
    return centroids

if __name__ == "__main__":
    points = [(0, 0), (1, 1), (0, 1), (1, 0), (5, 5), (6, 6), (5, 6), (6, 5)]
    k = 2
    centroids = k_means(points, k)
    print(f"The {k} centroids are: {centroids}")