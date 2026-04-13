Event Scheduler Extension (Lazy Updates & Cancellations)

## Overview

This project extends the Week 1 event scheduler by introducing two important behaviors commonly found in real-world systems:

* Dynamic priority updates
* Event cancellation before execution

The scheduler uses a **min-heap (`heapq`)** to efficiently determine the next event to process. Lower numeric priority values represent higher urgency.



## Implementation Details

### Priority Updates (Lazy Strategy)

Python’s heap implementation does not support direct priority modification. To address this, the scheduler applies a lazy update technique:

* A new heap entry is inserted with an incremented version number.
* Previous versions remain in the heap.
* When outdated entries reach the top, they are identified and discarded using version tracking.

This approach preserves efficiency while avoiding expensive heap restructuring.



### Event Cancellation

Cancellation is handled without directly removing elements from the heap:

* The event’s version reference is invalidated.
* The heap remains unchanged.
* Cancelled entries are skipped during peek and pop operations.

This ensures cancellation remains efficient and does not compromise heap performance.



## How to Run

```bash
python event_scheduler.py
```



## Sample Execution

```
=== Week 2 Simulation ===

[ADD]
Initial peek: (1, 101, 1, 'E2', 'Emergency supply: oxygen refill')

[PRIORITY UPDATE] E5 → 0
Peek after update: (0, 106, 2, 'E5', '[UPDATED] E5: 0')

[CANCELLATION] E3 removed
Peek after cancellation: (0, 106, 2, 'E5', '[UPDATED] E5: 0')

=== Final Processing Order ===
1. E5 (priority=0)
2. E2 (priority=1)
3. E4 (priority=1)
4. E6 (priority=2)
5. E1 (priority=3)
```



## Runtime Analysis

The dominant operations in this scheduler are heap insertions and removals, each running in **O(log n)** time. Every event addition, update, and processing step relies on these heap operations.

If a simple list were used instead, finding the highest-priority event would require scanning all elements, resulting in **O(n)** time per operation. As the number of events increases, this would significantly slow down the system.

Lazy updating is effective because it avoids costly in-place heap modifications. By inserting updated versions and ignoring outdated entries later, the scheduler maintains correctness while preserving efficient performance.

