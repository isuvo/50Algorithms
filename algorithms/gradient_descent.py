def gradient_descent(f, df, x0, lr=0.1, iterations=100):
    """Perform gradient descent on scalar function f.

    Time: O(iterations), Space: O(1)
    """
    x = x0
    for _ in range(iterations):
        x -= lr * df(x)
    return x, f(x)
