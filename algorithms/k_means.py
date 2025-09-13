import random

def k_means(points, k, iterations=10):
    """Cluster 2D points into k groups using k-means.

    Time: O(iterations * n * k), Space: O(k)
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
