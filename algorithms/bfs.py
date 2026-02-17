"""Breadth-First Search (BFS) Algorithm"""
from collections import deque
from utils.grid_utils import Node, get_neighbors, reconstruct_path


def bfs(grid, start, goal, visualizer=None):
    """
    Breadth-First Search algorithm
    Uses a queue (FIFO) to explore nodes level by level
    """
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    
    queue = deque([start_node])
    visited = {start_node}
    
    while queue:
        current = queue.popleft()
        
        # Visualize current state
        if visualizer:
            frontier = list(queue)
            visualizer.update(current, frontier, visited)
        
        # Check if goal reached
        if current == goal_node:
            return reconstruct_path(current), visited
        
        # Explore neighbors
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return None, visited  # No path found
