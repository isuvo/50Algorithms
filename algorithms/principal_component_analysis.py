"""
Principal Component Analysis (PCA).

This implementation of PCA finds the first principal component of a set of 2D
points. PCA is a statistical procedure that uses an orthogonal transformation
to convert a set of observations of possibly correlated variables into a set of
values of linearly uncorrelated variables called principal components.

Time Complexity: O(n), where n is the number of points.
Space Complexity: O(1)
"""
from typing import List, Tuple

Point = Tuple[float, float]

def pca(points: List[Point]) -> Point:
    """
    Return the first principal component for 2D data points.

    Args:
        points: A list of 2D points.

    Returns:
        The first principal component as a 2D vector.
    """
    n = len(points)
    mean_x = sum(p[0] for p in points) / n
    mean_y = sum(p[1] for p in points) / n
    cov_xx = sum((p[0] - mean_x) ** 2 for p in points) / n
    cov_xy = sum((p[0] - mean_x) * (p[1] - mean_y) for p in points) / n
    cov_yy = sum((p[1] - mean_y) ** 2 for p in points) / n
    trace = cov_xx + cov_yy
    det = cov_xx * cov_yy - cov_xy * cov_xy
    eigenvalue = trace / 2 + ((trace * trace / 4 - det) ** 0.5)
    eigenvector = (cov_xy, eigenvalue - cov_xx)
    norm = (eigenvector[0] ** 2 + eigenvector[1] ** 2) ** 0.5
    return (eigenvector[0] / norm, eigenvector[1] / norm)

if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    pc1 = pca(points)
    print(f"The first principal component is: {pc1}")