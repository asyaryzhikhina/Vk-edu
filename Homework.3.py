#Seminar 3.1.
#1. searchcomponents
def dfs(graph, v, visited, component):
    visited[v] = True
    component.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, component)

def find_connected_components(graph):
    visited = {node: False for node in graph}
    connected_components = []
    
    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            connected_components.append(component)
    
    return connected_components



#2. color
def dfs(graph, v, visited, color):
    visited[v] = color
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited, color)

def find_connected_components(graph):
    visited = {node: 0 for node in graph}
    color = 0
    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs(graph, node, visited, color)
    return visited

#3. searchcicles
def has_cycle(graph):
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            if dfs(graph, vertex, None, visited):
                return True
    return False

def dfs(graph, vertex, parent, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor != parent:
            if neighbor in visited or dfs(graph, neighbor, vertex, visited):
                return True
    return False

#4. trees
from collections import deque

def is_tree(graph, start):
    if not graph:  # пустой граф считается деревом
        return True
    
    visited = []
    queue = deque([start])
    parent = {start: None}
    
    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                if parent[vertex] != neighbor:
                    return False
    
    return len(visited) == len(graph)

#5. dijkstra

import heapq

def dijkstra(graph, start):
    # инициализация расстояний (бесконечность для всех вершин, кроме стартовой)
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # приоритетная очередь (куча) для хранения (расстояние, вершина)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # пропускаем, если нашли более короткий путь до этой вершины
        if current_distance > distances[current_vertex]:
            continue
        
        # обновляем расстояния до всех соседей
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # если нашли более короткий путь до соседа
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

#6. BFS

from collections import deque

def is_bipartite(graph):
    n = len(graph)
    colors = [0] * n 
    
    def bfs(start):
        queue = deque([start])
        colors[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        return True
    
    for i in range(n):
        if colors[i] == 0:
            if not bfs(i):
                return False
    return True

#7. DFS

def is_bipartite(graph):
    n = len(graph)
    colors = [0] * n  
    
    def dfs(node, c):
        colors[node] = c  
        for neighbor in graph[node]:
            if colors[neighbor] == 0:  
                if not dfs(neighbor, -c):  
                    return False
            elif colors[neighbor] == colors[node]:  
                return False
        return True
    
    for i in range(n):
        if colors[i] == 0: 
            if not dfs(i, 1):  
                return False
    return True

#Seminar 3.2.
#1. 
def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None
    
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

#2. 
from collections import defaultdict

def subarray_sum(nums, k):
    prefix_sum = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    count = 0

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1

    return count

#3. 0/1 подмассив
def find_max_length(nums):
    prefix_sum = 0
    max_len = 0
    index_map = {0: -1}  

    for i, num in enumerate(nums):
        prefix_sum += -1 if num == 0 else 1

        if prefix_sum in index_map:
            max_len = max(max_len, i - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i

    return max_len

#4. Индекс поворота
def pivot_index(nums):
    total_sum = sum(nums)  
    left_sum = 0           

    for i, num in enumerate(nums):
        if left_sum == total_sum - left_sum - num:
            return i
        
        left_sum += num

    return -1  
#5. Баланс скобок
def can_make_valid_with_deletions(s, k):
    balance = 0
    extra_closed = 0  

    for char in s:
        if char == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                extra_closed += 1

    total_deletions_needed = balance + extra_closed
    return total_deletions_needed <= k
