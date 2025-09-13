def strassen(a, b):
    """Multiply two square matrices using Strassen's algorithm.

    Time: O(n^{log2 7}), Space: O(n^2)
    """
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]
    mid = n // 2
    A11 = [row[:mid] for row in a[:mid]]
    A12 = [row[mid:] for row in a[:mid]]
    A21 = [row[:mid] for row in a[mid:]]
    A22 = [row[mid:] for row in a[mid:]]
    B11 = [row[:mid] for row in b[:mid]]
    B12 = [row[mid:] for row in b[:mid]]
    B21 = [row[:mid] for row in b[mid:]]
    B22 = [row[mid:] for row in b[mid:]]

    def add(X, Y):
        return [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(X, Y)]

    def sub(X, Y):
        return [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(X, Y)]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    top = [c1 + c2 for c1, c2 in zip(C11, C12)]
    bottom = [c1 + c2 for c1, c2 in zip(C21, C22)]
    return top + bottom
