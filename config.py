# Configuration file for AI Pathfinder

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

# Grid settings
GRID_SIZE = 15
CELL_SIZE = 30
MARGIN = 2

# Window settings
WINDOW_WIDTH = GRID_SIZE * (CELL_SIZE + MARGIN) + MARGIN + 300
WINDOW_HEIGHT = GRID_SIZE * (CELL_SIZE + MARGIN) + MARGIN + 100

# Algorithm settings
ANIMATION_DELAY = 0.05

# Movement directions
DIRECTIONS = [
    (-1, 0),   # Up
    (0, 1),    # Right
    (1, 0),    # Down
    (1, 1),    # Bottom-Right (diagonal)
    (0, -1),   # Left
    (-1, -1),  # Top-Left (diagonal)
]

# Cost for movements
STRAIGHT_COST = 1
DIAGONAL_COST = 1.414
