def fibonacci_series(n: int) -> list:
    """
    Generate Fibonacci series up to n terms using a loop.
    """
    if n <= 0:
        return []

    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    try:
        terms = int(input("Enter number of terms: "))

        if terms <= 0:
            print("Please enter a positive integer.")
        else:
            result = fibonacci_series(terms)
            print("Fibonacci Series:")
            print(result)

    except ValueError:
        print("Invalid input. Please enter an integer.")
