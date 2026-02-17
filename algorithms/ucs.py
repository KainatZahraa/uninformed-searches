"""Uniform Cost Search (UCS) Algorithm"""
import heapq
from utils.grid_utils import Node, get_neighbors, reconstruct_path


def ucs(grid, start, goal, visualizer=None):
    """
    Uniform Cost Search algorithm
    Uses a priority queue based on path cost
    """
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    start_node.g = 0
    
    # Priority queue: (cost, counter, node)
    # Counter ensures consistent ordering for nodes with same cost
    counter = 0
    priority_queue = [(0, counter, start_node)]
    visited = set()
    cost_so_far = {start_node: 0}
    
    while priority_queue:
        current_cost, _, current = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        # Visualize current state
        if visualizer:
            frontier = [node for _, _, node in priority_queue]
            visualizer.update(current, frontier, visited)
        
        # Check if goal reached
        if current == goal_node:
            return reconstruct_path(current), visited
        
        # Explore neighbors
        for neighbor in get_neighbors(current, grid):
            new_cost = current.g
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                neighbor.g = new_cost
                counter += 1
                heapq.heappush(priority_queue, (new_cost, counter, neighbor))
    
    return None, visited  # No path found
