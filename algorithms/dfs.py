"""Depth-First Search (DFS) Algorithm"""
from utils.grid_utils import Node, get_neighbors, reconstruct_path


def dfs(grid, start, goal, visualizer=None):
    """
    Depth-First Search algorithm
    Uses a stack (LIFO) to explore nodes depth-first
    """
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    
    stack = [start_node]
    visited = {start_node}
    
    while stack:
        current = stack.pop()
        
        # Visualize current state
        if visualizer:
            frontier = list(stack)
            visualizer.update(current, frontier, visited)
        
        # Check if goal reached
        if current == goal_node:
            return reconstruct_path(current), visited
        
        # Explore neighbors
        neighbors = get_neighbors(current, grid)
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    return None, visited  # No path found
