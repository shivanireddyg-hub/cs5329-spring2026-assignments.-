import timeit
import bisect

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    idx = bisect.bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    return -1

if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 200_000]
    runs = 1000

    for n in sizes:
        data = list(range(n))
        target = n - 1  # worst case

        linear_time = timeit.timeit(
            lambda: linear_search(data, target),
            number=runs
        )

        binary_time = timeit.timeit(
            lambda: binary_search(data, target),
            number=runs
        )

        print(
            f"n={n}: "
            f"Linear avg={linear_time / runs:.8f}s, "
            f"Binary avg={binary_time / runs:.8f}s"
        )
