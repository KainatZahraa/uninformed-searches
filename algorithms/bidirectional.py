"""Bidirectional Search Algorithm"""
from collections import deque
from utils.grid_utils import Node, get_neighbors, reconstruct_path


def bidirectional_search(grid, start, goal, visualizer=None):
    """
    Bidirectional Search algorithm
    Searches from both start and goal simultaneously
    """
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    
    # Forward search (from start)
    queue_forward = deque([start_node])
    visited_forward = {start_node: start_node}
    
    # Backward search (from goal)
    queue_backward = deque([goal_node])
    visited_backward = {goal_node: goal_node}
    
    while queue_forward and queue_backward:
        # Forward step
        if queue_forward:
            current_forward = queue_forward.popleft()
            
            # Check if forward search met backward search
            if current_forward in visited_backward:
                return merge_paths(current_forward, visited_forward, visited_backward), \
                       set(visited_forward.keys()) | set(visited_backward.keys())
            
            # Visualize
            if visualizer:
                all_frontier = list(queue_forward) + list(queue_backward)
                all_visited = set(visited_forward.keys()) | set(visited_backward.keys())
                visualizer.update(current_forward, all_frontier, all_visited)
            
            # Explore neighbors
            for neighbor in get_neighbors(current_forward, grid):
                if neighbor not in visited_forward:
                    visited_forward[neighbor] = current_forward
                    queue_forward.append(neighbor)
        
        # Backward step
        if queue_backward:
            current_backward = queue_backward.popleft()
            
            # Check if backward search met forward search
            if current_backward in visited_forward:
                return merge_paths(current_backward, visited_forward, visited_backward), \
                       set(visited_forward.keys()) | set(visited_backward.keys())
            
            # Visualize
            if visualizer:
                all_frontier = list(queue_forward) + list(queue_backward)
                all_visited = set(visited_forward.keys()) | set(visited_backward.keys())
                visualizer.update(current_backward, all_frontier, all_visited)
            
            # Explore neighbors
            for neighbor in get_neighbors(current_backward, grid):
                if neighbor not in visited_backward:
                    visited_backward[neighbor] = current_backward
                    queue_backward.append(neighbor)
    
    return None, set(visited_forward.keys()) | set(visited_backward.keys())


def merge_paths(meeting_point, visited_forward, visited_backward):
    """
    Merge paths from forward and backward searches
    """
    # Build forward path
    path_forward = []
    current = meeting_point
    while current is not None:
        path_forward.append((current.row, current.col))
        parent = visited_forward.get(current)
        if parent == current:  
            break
        current = parent
    path_forward.reverse()
    
    # Build backward path
    path_backward = []
    current = visited_backward.get(meeting_point)
    if current != meeting_point: 
        while current is not None:
            path_backward.append((current.row, current.col))
            parent = visited_backward.get(current)
            if parent == current: 
                break
            current = parent
    
    return path_forward + path_backward
