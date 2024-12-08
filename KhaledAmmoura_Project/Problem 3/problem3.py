from collections import deque

def minimum_swaps(graph, control, target):
    if control == target:
        return 0
    queue = deque([(control, 0)])
    visited= set()
    visited.add(control)

    while queue:
        current, distance = queue.popleft()
        if current == target:
            return (distance -1)*2 # we multiplied by 2 to return it to its original position
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance+1))
    
    return -1

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4]
}

control = 0
target = 8
result = minimum_swaps(graph, control, target)
print(f"Minimum number of SWAP gates required: {result}")