# Linear Search vs Binary Search (Timing Comparison)

## Overview
This Python program compares the performance of **Linear Search** and **Binary Search** by measuring how long each takes to find a target element in arrays of different sizes.

The purpose of the program is to demonstrate the difference between:
- **Linear Search** → `O(n)`
- **Binary Search** → `O(log n)` (only works on sorted arrays)



## What the Program Does
For each array size, the program:
1. Creates a sorted list of integers from `0` to `n-1`
2. Selects the target as the last element (`n-1`) to simulate the **worst case** for linear search
3. Runs both search functions multiple times (`runs = 1000`)
4. Prints the **average runtime per search** in seconds



## Algorithms Implemented

### Linear Search
Checks elements one by one until the target is found.

### Binary Search
Uses Python’s built-in `bisect_left()` method to locate the target efficiently.


## How to Run
Make sure Python 3 is installed, then run:

```bash
python3 linear_vs_binary_search.py
