"""Depth-Limited Search (DLS) Algorithm"""
from utils.grid_utils import Node, get_neighbors, reconstruct_path

def dls_recursive(current, goal_node, grid, depth_limit, visited, visualizer=None, frontier=None):
    """
    Recursive helper for DLS
    """
    if frontier is None:
        frontier = []
    
    # Visualize current state
    if visualizer:
        visualizer.update(current, frontier, visited)
    
    # Check if goal reached
    if current == goal_node:
        return reconstruct_path(current)
    
    # Check depth limit
    if depth_limit == 0:
        return "cutoff"
    
    visited.add(current)
    cutoff_occurred = False
    
    # Explore neighbors
    for neighbor in get_neighbors(current, grid):
        if neighbor not in visited:
            frontier.append(neighbor)
            result = dls_recursive(neighbor, goal_node, grid, depth_limit - 1, visited, visualizer, frontier)
            frontier.remove(neighbor)
            
            if result == "cutoff":
                cutoff_occurred = True
            elif result is not None:
                return result
    
    if cutoff_occurred:
        return "cutoff"
    return None


def dls(grid, start, goal, depth_limit=15, visualizer=None):
    """
    Depth-Limited Search algorithm
    DFS with a maximum depth limit
    """
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    
    visited = set()
    result = dls_recursive(start_node, goal_node, grid, depth_limit, visited, visualizer)
    
    if result == "cutoff" or result is None:
        return None, visited
    return result, visited
