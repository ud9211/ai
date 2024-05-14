def bestfs(graph,start,goal,heuri):
    queue=[(start,[start])]
    visited=set()

    while queue:
        current,path=queue.pop(0)
        if current==goal:
            return path
        if current not in visited:
            visited.add(current)

            for i in graph[current]:
                if i not in visited:
                    queue.append((i,path+[i]))
            queue.sort(key=lambda x: heuri[x[0]])
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['H'],
    'G': [],
    'H': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0,
    'H': 3
}

start, goal= 'A','G'
path=bestfs(graph,start,goal,heuristic)
if path:
    print(f"This is the final path :{path}")
else:
    print("no path")