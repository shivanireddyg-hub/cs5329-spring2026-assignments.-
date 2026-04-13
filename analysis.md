## Part 1 — Greedy Strategy Design

### Strategy 1: Earliest Finish with Constraint Validation

**Greedy-choice idea.**
This approach selects tasks based on increasing finishing time while ensuring feasibility under both resource and category constraints. The intuition is that tasks that finish earlier release both time and resource capacity sooner, which preserves flexibility for scheduling future tasks. This is inspired by the classical interval scheduling problem where earliest finish time guarantees optimality under simple constraints. However, in this problem, feasibility must also consider resource accumulation and category overlap limits, making the greedy step conditional.

This strategy works well when tasks are loosely distributed across time and when resource usage is not the dominant bottleneck. In sparse environments, selecting early-finishing tasks allows the scheduler to pack more tasks overall because fewer conflicts arise later. It also performs well when weights are relatively uniform, since prioritizing time efficiency aligns with maximizing total selection.

However, the strategy can fail when weight distribution is uneven. Consider `R = 6` and `K = 2`. Suppose there are five short tasks each with weight `2` that fill small intervals sequentially, and one long task with weight `15` spanning the entire period. The greedy method will pick all short tasks due to their earlier finishing times, achieving a total weight of `10`, while the optimal solution would choose the single long task with weight `15`. This illustrates that prioritizing temporal efficiency can overlook globally optimal high-value decisions.

---

### Strategy 2: Highest Weight-to-Resource Ratio

**Greedy-choice idea.**
This strategy prioritizes tasks based on their efficiency, defined as `weight / resource`. The goal is to maximize the value gained per unit of resource consumed. Since resource capacity is a limiting factor across overlapping intervals, this metric attempts to use resources as efficiently as possible. Tasks are selected in descending order of this ratio, with feasibility checks ensuring constraints are respected.

This method performs well when resource contention is the primary challenge. In dense scenarios where many tasks overlap, prioritizing efficient tasks allows the scheduler to fit more value into limited capacity. It is especially effective when tasks vary widely in resource requirements, as it avoids selecting resource-heavy tasks with low returns.

A failure case occurs when a single high-ratio task blocks multiple medium-value tasks. For example, let `R = 4` and `K = 2`. Suppose task `A = (0,10,8,1)` with ratio `8`, and two tasks `B1 = (0,5,6,2)` and `B2 = (5,10,6,2)` with ratio `3`. The greedy strategy selects `A` first, leaving insufficient capacity for both `B` tasks. The total becomes `8`, while the optimal is `12`. This demonstrates that maximizing local efficiency does not always lead to the best global combination.

---

## Part 2 — Brute-Force Baseline

The brute-force solution evaluates all possible subsets for small inputs (`n ≤ 15`) and selects the feasible subset with maximum total weight. It guarantees optimality by exhaustively checking all combinations against time, resource, and category constraints.

The following table summarizes validation results:

| Validation case           | Optimal weight | Earliest-finish quality | Ratio quality | Time (s) |
| ------------------------- | -------------: | ----------------------: | ------------: | -------: |
| validation_sparse_8       |          42.10 |                 100.00% |       100.00% |   0.0003 |
| validation_dense_10       |          20.50 |                  80.12% |        85.90% |   0.0025 |
| validation_category_12    |          28.30 |                 100.00% |       100.00% |   0.0090 |
| validation_adversarial_10 |          13.00 |                  74.00% |       100.00% |   0.0021 |
| validation_identical_6    |          18.00 |                 100.00% |       100.00% |   0.0002 |

On average, earliest-finish achieved **90–92%**, while the ratio strategy achieved **95–97%** of optimal.

---

## Part 3 — Benchmarking and Analysis

### Scenario Design

Four categories of test data were generated:

1. **Sparse:** Low overlap, high resource availability
2. **Dense:** Heavy overlap, limited capacity
3. **Category-heavy:** Many tasks share the same category with small `K`
4. **Adversarial:** Designed to mislead greedy heuristics

---

### Runtime Comparison

| n    | Earliest-finish (s) | Ratio (s) |
| ---- | ------------------: | --------: |
| 10   |             0.00005 |   0.00004 |
| 50   |             0.00040 |   0.00030 |
| 100  |             0.00060 |   0.00055 |
| 500  |             0.00600 |   0.00720 |
| 1000 |             0.01500 |   0.02000 |

---

### Quality Comparison (n = 10)

| Scenario       | Earliest | Ratio |
| -------------- | -------: | ----: |
| sparse         |     100% |  100% |
| dense          |      82% |   88% |
| category-heavy |      78% |   93% |
| adversarial    |      70% |  100% |

---

### Analysis 

The experimental results show that the **weight-to-resource ratio strategy consistently outperforms earliest-finish in most constrained scenarios**. This is particularly evident in dense and category-heavy cases, where resource limitations and overlap conflicts dominate decision-making. By prioritizing value efficiency, the ratio method is better able to allocate scarce resources to high-impact tasks.

In contrast, the earliest-finish strategy performs best in sparse environments. When conflicts are minimal, selecting tasks that end early allows for more total tasks to be scheduled, which often leads to optimal or near-optimal solutions. However, its weakness becomes clear in adversarial setups, where it prioritizes short-duration tasks regardless of their contribution to total weight.

The adversarial scenario highlights the difference clearly. By constructing tasks with short durations but low weights alongside a long high-weight task, earliest-finish is misled into selecting many low-value tasks. The ratio strategy, however, immediately selects the high-value task and achieves optimal performance.

Category constraints introduce another layer of complexity. When many tasks share the same category, the limit `K` restricts how many can overlap. This reduces the effectiveness of both greedy strategies because decisions must now consider category availability in addition to time and resources. In some large category-heavy cases, earliest-finish slightly outperformed the ratio strategy because it naturally spread tasks across time, indirectly avoiding category conflicts.

Overall, while the ratio strategy performs better in most cases, neither approach is universally optimal. Each heuristic has strengths tied to specific structural properties of the input.

---

## Part 4 — Reflection

This problem does not admit a universally optimal greedy solution because decisions have **global consequences across multiple dimensions**: time overlap, resource capacity, and category limits. A locally optimal choice may prevent better combinations later, violating the greedy-choice property.

For greedy optimality, the problem would need stronger mathematical structure, such as independence systems or matroid properties, where local decisions can always be extended to a global optimum. Classic interval scheduling satisfies this, but adding weights, resources, and categories breaks that structure.

In a real-world system, I would combine greedy heuristics with more powerful optimization methods. For example, greedy could provide an initial feasible solution, which is then improved using techniques like integer linear programming, constraint solvers, or local search. This hybrid approach balances efficiency with solution quality.

---

