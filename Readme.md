# Activity 2.1 – Recurrence Experimentation and Analysis

Course: CS 5329 – Algorithm Design and Analysis
Student Name: Shivani Guda
Net ID: epb44
Semester: Spring 2026



# Overview

This assignment compares two different approaches for computing Fibonacci numbers: a simple recursive method and a dynamic programming (memoized) method. The goal is to observe how their performance changes as the input size increases and to understand the effect of overlapping subproblems in recursive algorithms.



# How to Run the Code

From the project directory, run the following command:

'''bash
python assignment2_fibonacci.py



# Sample Output


n=10: fib_recursive -> 55 (time 0.0001s), fib_dp -> 55 (time 0.0000s)
n=20: fib_recursive -> 6765 (time 0.0013s), fib_dp -> 6765 (time 0.0000s)
n=30: fib_recursive -> 832040 (time 0.1420s), fib_dp -> 832040 (time 0.0001s)
n=35: fib_recursive -> 9227465 (time 1.5124s), fib_dp -> 9227465 (time 0.0001s)



# Analysis Questions and Answers

a. Why does `fib_recursive` slow down so dramatically as n increases?

The recursive version becomes slow because it solves the same subproblems multiple times. Each call to the function creates two additional calls, which leads to a rapidly growing number of total calls. As *n* increases, this repeated work causes the running time to grow very quickly.

b. What is the Big-O time complexity of each approach?

`fib_recursive` has exponential time complexity, approximately O(2ⁿ), because the number of recursive calls increases rapidly with *n*.
`fib_dp` has linear time complexity, O(n), since each Fibonacci value is computed once and then stored for reuse.

c. Would `fib_recursive(50)` be feasible? Explain your reasoning.

No, it would not be practical to compute `fib_recursive(50)`. The recursive approach would generate a huge number of function calls, making the program extremely slow. For larger inputs, the dynamic programming approach is much more efficient and practical.


d. How does memoization change the nature of the recurrence?

Memoization stores the result of each computed Fibonacci number so it can be reused later. Instead of recalculating the same values repeatedly, the program looks them up from memory.This removes redundant computations and reduces the time complexity from exponential to linear.

