def pca(points):
    """Return the first principal component for 2D data points.

    Time: O(n), Space: O(1)
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
