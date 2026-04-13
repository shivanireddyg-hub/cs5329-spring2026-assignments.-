import time


def fib_rec(k):
    if k == 0 or k == 1:
        return k
    return fib_rec(k - 1) + fib_rec(k - 2)


def fib_fast(k):
    if k == 0:
        return 0
    if k == 1:
        return 1

    prev = 0
    curr = 1

    for _ in range(k - 1):
        prev, curr = curr, prev + curr
    return curr


def run_small_tests(values):
    print("==== Fibonacci Timing: Recursive vs DP ====\n")

    for n in values:
        t0 = time.perf_counter()
        ans1 = fib_rec(n)
        t1 = time.perf_counter() - t0

        t0 = time.perf_counter()
        ans2 = fib_fast(n)
        t2 = time.perf_counter() - t0

        print(f"n={n}")
        print(f"  Recursive Result: {ans1} | Time: {t1:.5f} sec")
        print(f"  DP Result       : {ans2} | Time: {t2:.8f} sec")
        print("-" * 45)


def run_large_tests(values):
    print("\n==== Large Fibonacci Tests (DP only) ====\n")
    for n in values:
        t0 = time.perf_counter()
        fib_fast(n)
        elapsed = time.perf_counter() - t0
        print(f"DP Fibonacci n={n} -> time: {elapsed:.8f} sec")


if __name__ == "__main__":
    small_vals = [10, 20, 30, 35]
    large_vals = [50, 100, 500, 1000]

    run_small_tests(small_vals)
    run_large_tests(large_vals)
