A heap is better than a list/array because it always keeps the most urgent event at the top with O(log n) inserts/removals, while a list would require scanning/sorting.  
The operation performed repeatedly is selecting the next event (peek/pop) many times as requests arrive.  
Using versioning lets the scheduler skip outdated or cancelled events efficiently.
