"""Utility functions for grid operations and node handling"""
import random
from config import GRID_SIZE, DIRECTIONS, STRAIGHT_COST, DIAGONAL_COST


class Node:
    """Represents a node in the grid"""
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent
        self.g = 0  # Cost from start
        self.h = 0  # Heuristic to goal
        self.f = 0  # Total cost (g + h)
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def __hash__(self):
        return hash((self.row, self.col))
    
    def __lt__(self, other):
        return self.f < other.f


def is_valid_position(row, col, grid):
    """Check if position is valid and not a wall"""
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        return grid[row][col] != 1  # 1 represents wall
    return False


def get_neighbors(node, grid):
    """Get all valid neighbors of a node in the specified order"""
    neighbors = []
    row, col = node.row, node.col
    
    for i, (dr, dc) in enumerate(DIRECTIONS):
        new_row, new_col = row + dr, col + dc
        if is_valid_position(new_row, new_col, grid):
            neighbor = Node(new_row, new_col, node)
            # Calculate cost based on movement type
            if i in [0, 1, 2, 4]:  # Straight movements
                neighbor.g = node.g + STRAIGHT_COST
            else:  # Diagonal movements
                neighbor.g = node.g + DIAGONAL_COST
            neighbors.append(neighbor)
    
    return neighbors


def manhattan_distance(node1, node2):
    """Calculate Manhattan distance heuristic"""
    return abs(node1.row - node2.row) + abs(node1.col - node2.col)


def euclidean_distance(node1, node2):
    """Calculate Euclidean distance heuristic"""
    return ((node1.row - node2.row)**2 + (node1.col - node2.col)**2)**0.5


def reconstruct_path(node):
    """Reconstruct path from goal to start"""
    path = []
    current = node
    while current is not None:
        path.append((current.row, current.col))
        current = current.parent
    return path[::-1]


def initialize_grid():
    """Initialize an empty grid"""
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def add_random_walls(grid, num_walls=50):
    """Add random walls to the grid"""
    walls_added = 0
    while walls_added < num_walls:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if grid[row][col] == 0:
            grid[row][col] = 1
            walls_added += 1
