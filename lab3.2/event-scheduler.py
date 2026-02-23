import heapq

def create_scheduler():
    heap = []
    current_version = {}  # event_id -> latest version (None means cancelled)
    return heap, current_version

def add_event(heap, current_version, event_id, priority, created_time, payload):
    v = current_version.get(event_id, 0) + 1
    current_version[event_id] = v
    heapq.heappush(heap, (priority, created_time, v, event_id, payload))

def update_priority(heap, current_version, event_id, new_priority, update_time):
    """
    Lazily updates an event's priority by pushing a new (versioned) entry.
    Old entries stay in the heap and will be skipped later.
    Returns True if updated, False if event doesn't exist or is cancelled.
    """
    latest = current_version.get(event_id, None)
    if latest is None:
        return False  # cancelled or never existed

    v = latest + 1
    current_version[event_id] = v
    # payload is not required for correctness; keep a small payload describing update
    payload = {"type": "priority_update", "new_priority": new_priority}
    heapq.heappush(heap, (new_priority, update_time, v, event_id, payload))
    return True

def cancel_event(current_version, event_id):
    """
    Cancels an event so it will never be processed.
    (We don't remove from heap; discard_stale_top will skip it later.)
    Returns True if it was present, False if it was already absent/cancelled.
    """
    existed = event_id in current_version and current_version.get(event_id, None) is not None
    current_version[event_id] = None
    return existed

def discard_stale_top(heap, current_version):
    while heap:
        priority, created_time, v, event_id, payload = heap[0]
        latest = current_version.get(event_id, None)
        if latest is None or latest != v:
            heapq.heappop(heap)
            continue
        break

def peek_next(heap, current_version):
    discard_stale_top(heap, current_version)
    if not heap:
        return None
    return heap[0]

def pop_next(heap, current_version):
    discard_stale_top(heap, current_version)
    if not heap:
        return None
    return heapq.heappop(heap)

def main():
    heap, current_version = create_scheduler()

    print("=== ADD EVENTS ===")
    add_event(heap, current_version, "E1", 2, 1, {"msg": "Pay electricity bill"})
    add_event(heap, current_version, "E2", 1, 2, {"msg": "Production alert"})
    add_event(heap, current_version, "E3", 3, 3, {"msg": "Clinic intake"})
    add_event(heap, current_version, "E4", 1, 4, {"msg": "Security incident"})
    add_event(heap, current_version, "E5", 0, 7, {"msg": "URGENT: Send report now"})
    add_event(heap, current_version, "E6", 1, 6, {"msg": "Database backup"})

    print("Peek after adds:", peek_next(heap, current_version))

    print("\n=== UPDATE PRIORITY (LAZY) ===")
    updated = update_priority(heap, current_version, "E3", new_priority=0, update_time=8)
    print("Updated E3 to priority 0:", updated)
    print("Peek after update:", peek_next(heap, current_version))

    print("\n=== CANCEL EVENT (LAZY) ===")
    cancelled = cancel_event(current_version, "E4")
    print("Cancelled E4:", cancelled)
    print("Peek after cancel:", peek_next(heap, current_version))

    print("\n=== FINAL PROCESSING ORDER (POP UNTIL EMPTY) ===")
    while True:
        ev = pop_next(heap, current_version)
        if ev is None:
            break
        print(ev)

if __name__ == "__main__":
    main()