Runtime Thinking (Mini-Analysis)

The operation that dominates runtime in this scheduler is heap insertion and removal, both of which run in O(log n) time. Every add, update, and pop operation depends on these heap operations, making them the primary cost in the system.

Scanning a list would be inefficient because finding the highest-priority event would require O(n) time each time an event is processed. As the number of events grows, repeated scanning would significantly increase total runtime.

Lazy updating is acceptable in practice because it avoids expensive in-place heap modifications. Instead of restructuring the heap, we insert a new version and skip outdated entries later, maintaining correctness while preserving efficient performance.