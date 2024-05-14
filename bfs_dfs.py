from collections import deque

graph={
    'a':['b','c'],
    'b':['a','d','e'],
    'c':['a','f','g'],
    'd':['b'],
    'e':['b','h'],
    'f':['c'],
    'g':['c'],
    'h':['e']
}

def bfs(graph, start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(i for i in graph[node] if i not in visited)

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for i in graph[node]:
            dfs(graph,i,visited)

start_node='a'
visited_node=set()
print("dfs: ")
dfs(graph,start_node,visited_node)
print('\n')
print("bfs: ")
bfs(graph, start_node)