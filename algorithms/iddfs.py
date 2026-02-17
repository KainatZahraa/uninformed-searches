"""Iterative Deepening Depth-First Search (IDDFS) Algorithm"""
from algorithms.dls import dls_recursive
from utils.grid_utils import Node


def iddfs(grid, start, goal, max_depth=30, visualizer=None):
    """
    Iterative Deepening DFS algorithm
    Performs DLS with increasing depth limits
    """
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    
    all_visited = set()
    
    # Try increasing depths
    for depth in range(max_depth):
        visited = set()
        result = dls_recursive(start_node, goal_node, grid, depth, visited, visualizer)
        all_visited.update(visited)
        
        if result != "cutoff" and result is not None:
            return result, all_visited
    
    return None, all_visited  # No path found
