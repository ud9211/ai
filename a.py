import heapq

def a_star(graph, start, goal, heuristic):

    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {start: 0}
    
    came_from = {start: None}
    
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            tentative_g_cost = g_cost[current_node] + weight
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_node
    
    return None
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 1},
    'E': {'B': 5, 'G': 2},
    'F': {'C': 3, 'H': 1},
    'G': {'D': 1, 'E': 2, 'H': 6},
    'H': {'F': 1, 'G': 6}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 4,
    'F': 3,
    'G': 0,
    'H': 6
}

start, goal = 'A', 'G'
path = a_star(graph, start, goal, heuristic)
if path:
    print("This is the final path: " + ' -> '.join(path))
else:
    print("No path found from {} to {}".format(start, goal))
