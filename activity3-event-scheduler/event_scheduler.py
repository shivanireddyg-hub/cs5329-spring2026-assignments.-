import heapq

def create_scheduler():
    heap = []
    current_version = {}
    return heap, current_version

def add_event(heap, current_version, event_id, priority, created_time, payload):
    v = current_version.get(event_id, 0) + 1
    current_version[event_id] = v
    heapq.heappush(heap, (priority, created_time, v, event_id, payload))

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

    add_event(heap, current_version, "E1", 2, 1, {"msg": "Pay electricity bill"})
    add_event(heap, current_version, "E2", 1, 2, {"msg": "Production alert"})
    add_event(heap, current_version, "E3", 3, 3, {"msg": "Clinic intake"})
    add_event(heap, current_version, "E4", 1, 4, {"msg": "Security incident"})
    add_event(heap, current_version, "E5", 0, 7, {"msg": "URGENT: Send report now"})
    add_event(heap, current_version, "E6", 1, 6, {"msg": "Database backup"})

    print("peek_next:", peek_next(heap, current_version))

    print("processing order (pop until empty):")
    while True:
        ev = pop_next(heap, current_version)
        if ev is None:
            break
        print(ev)

if __name__ == "__main__":
    main()
