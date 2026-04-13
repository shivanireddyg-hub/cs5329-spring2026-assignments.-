# Multi-Constraint Greedy Resource Scheduler

## Overview

This project implements a scheduling system for tasks with multiple constraints, including time windows, resource usage, and category limits. The objective is to select a subset of tasks that maximizes total weight while satisfying all constraints.

The system includes:

* Two greedy strategies
* A brute-force solver for optimal solutions on small inputs
* A test case generator
* Benchmarking support for performance evaluation

---

## Project Structure

greedy-scheduler/

* scheduler.py → Main implementation (greedy + brute force)
* test_generator.py → Generates test cases
* analysis.md → Written explanations and analysis
* README.md → Instructions

Folders:

* test_cases/ → Input JSON files
* results/ → Output JSON files

---

## Requirements

* Python 3.8 or higher
* No external libraries required

---

## How to Run

### 1. Generate Test Cases

python3 test_generator.py --output-dir test_cases

This creates multiple test files such as:

* sparse_10.json
* dense_100.json
* category_heavy_50.json
* adversarial_10.json

---

### 2. Run Scheduler

Use the solve command:

python3 scheduler.py solve --input test_cases/sparse_10.json --strategy earliest_finish_resource_aware --output results/output.json

---

## Available Strategies

* earliest_finish_resource_aware
* highest_weight_to_resource_ratio
* brute_force_optimal (only for small inputs n ≤ 15)

---

## Example Runs

Earliest Finish:
python3 scheduler.py solve --input test_cases/sparse_10.json --strategy earliest_finish_resource_aware --output results/sparse_earliest.json

Ratio Strategy:
python3 scheduler.py solve --input test_cases/sparse_10.json --strategy highest_weight_to_resource_ratio --output results/sparse_ratio.json

Brute Force:
python3 scheduler.py solve --input test_cases/sparse_10.json --strategy brute_force_optimal --output results/sparse_optimal.json

---

## Output Format

Each run generates a JSON file containing:

* selected_tasks
* total_weight
* execution_time_seconds
* utilization_timeline

Example:

{
"strategy_name": "earliest_finish_resource_aware",
"selected_tasks": [0, 1, 2],
"total_weight": 25.5,
"execution_time_seconds": 0.0012,
"utilization_timeline": {
"0-5": {
"resource_used": 3,
"categories": {"compute": 1}
}
}
}

---

## Benchmarking

To evaluate performance:

* Run both greedy strategies on all test cases
* Use brute-force for small inputs as the optimal baseline
* Compare total weight and execution time

---

## Notes

* Brute-force is exponential, so use only for small inputs
* Greedy strategies are fast but may not always be optimal
* Category constraints make the problem more complex than standard scheduling

---

## Submission Checklist

Make sure your submission includes:

* scheduler.py
* test_generator.py
* test_cases/
* results/
* analysis.md
* README.md

---

## Author

Developed as part of an algorithm design assignment on greedy scheduling and optimization.
