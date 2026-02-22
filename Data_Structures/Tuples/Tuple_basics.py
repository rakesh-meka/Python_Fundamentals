"""Tuple interview questions and answers in Python.

This script collects important and frequently asked tuple-based interview
questions with short, runnable solutions.
"""


def reverse_tuple(values: tuple) -> tuple:
    """Q1: Reverse a tuple."""
    return values[::-1]


def remove_duplicates_preserve_order(values: tuple) -> tuple:
    """Q2: Remove duplicates from a tuple while keeping order."""
    seen = set()
    result = []
    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return tuple(result)


def second_largest(values: tuple[int, ...]) -> int | None:
    """Q3: Find the second largest element in a tuple.

    Returns None when second largest does not exist.
    """
    unique_values = sorted(set(values))
    if len(unique_values) < 2:
        return None
    return unique_values[-2]


def flatten_tuple(nested: tuple) -> tuple:
    """Q4: Flatten a nested tuple recursively."""
    flat = []

    for element in nested:
        if isinstance(element, tuple):
            flat.extend(flatten_tuple(element))
        else:
            flat.append(element)

    return tuple(flat)


def is_palindrome(values: tuple) -> bool:
    """Q5: Check if a tuple is palindrome."""
    return values == values[::-1]


def swap_first_last(values: tuple) -> tuple:
    """Q6: Swap first and last elements of a tuple."""
    if len(values) < 2:
        return values
    return (values[-1],) + values[1:-1] + (values[0],)


def tuple_frequency(values: tuple) -> dict:
    """Q7: Count frequency of each element in a tuple."""
    frequency = {}
    for item in values:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency


def common_elements(first: tuple, second: tuple) -> tuple:
    """Q8: Find common elements between two tuples (unique)."""
    return tuple(sorted(set(first) & set(second)))


def run_examples() -> None:
    """Run all interview-style examples."""
    nums = (10, 20, 30, 40, 30, 20)
    nested = (1, (2, 3), (4, (5, 6)), 7)
    pal = (1, 2, 3, 2, 1)
    not_pal = (1, 2, 3)
    a = (1, 2, 3, 4)
    b = (3, 4, 5, 6)

    print("Q1 Reverse tuple:", reverse_tuple(nums))
    print("Q2 Remove duplicates:", remove_duplicates_preserve_order(nums))
    print("Q3 Second largest:", second_largest(nums))
    print("Q4 Flatten nested tuple:", flatten_tuple(nested))
    print("Q5 Palindrome check (pal):", is_palindrome(pal))
    print("Q5 Palindrome check (not_pal):", is_palindrome(not_pal))
    print("Q6 Swap first/last:", swap_first_last((11, 22, 33, 44)))
    print("Q7 Frequency map:", tuple_frequency(nums))
    print("Q8 Common elements:", common_elements(a, b))


if __name__ == "__main__":
    run_examples()
