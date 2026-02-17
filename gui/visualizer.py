"""GUI Visualizer for Pathfinding Algorithms using Pygame"""
import pygame
import time
from config import *
from utils.grid_utils import add_dynamic_obstacle


class PathfindingVisualizer:
    """Main visualizer class for pathfinding algorithms"""
    
    def __init__(self, grid, start, goal, algorithm_name):
        pygame.init()
        self.grid = grid
        self.start = start
        self.goal = goal
        self.algorithm_name = algorithm_name
        

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(f"GOOD PERFORMANCE TIME APP - {algorithm_name}")
        
        # Fonts
        self.font = pygame.font.SysFont('Arial', 16)
        self.title_font = pygame.font.SysFont('Arial', 24, bold=True)
        
        # Stats
        self.nodes_explored = 0
        self.path_length = 0
        self.dynamic_obstacles = []
        
    def draw_grid(self):
        """Draw the grid with cells"""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * (CELL_SIZE + MARGIN) + MARGIN
                y = row * (CELL_SIZE + MARGIN) + MARGIN
                
                # Determine color based on cell type
                if self.grid[row][col] == 1:
                    color = BLACK  # Wall
                elif (row, col) == (self.start[0], self.start[1]):
                    color = BLUE  # Start
                elif (row, col) == (self.goal[0], self.goal[1]):
                    color = GREEN  # Goal
                else:
                    color = WHITE  # Empty
                
                pygame.draw.rect(self.screen, color, (x, y, CELL_SIZE, CELL_SIZE))
    
    def draw_exploration(self, current, frontier, visited):
        """Draw the exploration state"""
        # Draw visited nodes
        for node in visited:
            if (node.row, node.col) != (self.start[0], self.start[1]) and \
               (node.row, node.col) != (self.goal[0], self.goal[1]):
                x = node.col * (CELL_SIZE + MARGIN) + MARGIN
                y = node.row * (CELL_SIZE + MARGIN) + MARGIN
                pygame.draw.rect(self.screen, CYAN, (x, y, CELL_SIZE, CELL_SIZE))
        
        # Draw frontier nodes
        for node in frontier:
            if (node.row, node.col) != (self.start[0], self.start[1]) and \
               (node.row, node.col) != (self.goal[0], self.goal[1]):
                x = node.col * (CELL_SIZE + MARGIN) + MARGIN
                y = node.row * (CELL_SIZE + MARGIN) + MARGIN
                pygame.draw.rect(self.screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))
        
        # Draw current node
        if current and (current.row, current.col) != (self.start[0], self.start[1]) and \
           (current.row, current.col) != (self.goal[0], self.goal[1]):
            x = current.col * (CELL_SIZE + MARGIN) + MARGIN
            y = current.row * (CELL_SIZE + MARGIN) + MARGIN
            pygame.draw.rect(self.screen, ORANGE, (x, y, CELL_SIZE, CELL_SIZE))
        
        # Redraw start and goal
        start_x = self.start[1] * (CELL_SIZE + MARGIN) + MARGIN
        start_y = self.start[0] * (CELL_SIZE + MARGIN) + MARGIN
        pygame.draw.rect(self.screen, BLUE, (start_x, start_y, CELL_SIZE, CELL_SIZE))
        
        goal_x = self.goal[1] * (CELL_SIZE + MARGIN) + MARGIN
        goal_y = self.goal[0] * (CELL_SIZE + MARGIN) + MARGIN
        pygame.draw.rect(self.screen, GREEN, (goal_x, goal_y, CELL_SIZE, CELL_SIZE))
    
    def draw_path(self, path):
        """Draw the final path"""
        if path:
            for i, (row, col) in enumerate(path):
                if (row, col) != (self.start[0], self.start[1]) and \
                   (row, col) != (self.goal[0], self.goal[1]):
                    x = col * (CELL_SIZE + MARGIN) + MARGIN
                    y = row * (CELL_SIZE + MARGIN) + MARGIN
                    pygame.draw.rect(self.screen, PURPLE, (x, y, CELL_SIZE, CELL_SIZE))
    
    def draw_stats(self):
        """Draw statistics on the screen"""
        stats_x = GRID_SIZE * (CELL_SIZE + MARGIN) + 20
        stats_y = 20
        
        # Title
        title_text = self.title_font.render(self.algorithm_name, True, BLACK)
        self.screen.blit(title_text, (stats_x, stats_y))
        
        # Stats
        stats = [
            f"Nodes Explored: {self.nodes_explored}",
            f"Path Length: {self.path_length}",
            f"Dynamic Obstacles: {len(self.dynamic_obstacles)}",
            "",
            "Legend:",
            "Blue = Start",
            "Green = Goal",
            "Black = Wall",
            "Cyan = Visited",
            "Yellow = Frontier",
            "Orange = Current",
            "Purple = Path"
        ]
        
        for i, stat in enumerate(stats):
            text = self.font.render(stat, True, BLACK)
            self.screen.blit(text, (stats_x, stats_y + 40 + i * 25))
    
    def update(self, current, frontier, visited):
        """Update the visualization"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        self.nodes_explored = len(visited)
        
        # Check for dynamic obstacles
        obstacle = add_dynamic_obstacle(self.grid, self.start, self.goal, 
                                       DYNAMIC_OBSTACLE_PROBABILITY)
        if obstacle:
            self.dynamic_obstacles.append(obstacle)
        
        # Draw everything
        self.screen.fill(WHITE)
        self.draw_grid()
        self.draw_exploration(current, frontier, visited)
        self.draw_stats()
        
        pygame.display.flip()
        time.sleep(ANIMATION_DELAY)
    
    def show_result(self, path, visited):
        """Show the final result"""
        self.path_length = len(path) if path else 0
        
        # Final update
        self.screen.fill(WHITE)
        self.draw_grid()
        
        # Draw all visited nodes
        for node in visited:
            if (node.row, node.col) != (self.start[0], self.start[1]) and \
               (node.row, node.col) != (self.goal[0], self.goal[1]):
                x = node.col * (CELL_SIZE + MARGIN) + MARGIN
                y = node.row * (CELL_SIZE + MARGIN) + MARGIN
                pygame.draw.rect(self.screen, CYAN, (x, y, CELL_SIZE, CELL_SIZE))
        
        # Draw path
        if path:
            self.draw_path(path)
        
        # Redraw start and goal
        start_x = self.start[1] * (CELL_SIZE + MARGIN) + MARGIN
        start_y = self.start[0] * (CELL_SIZE + MARGIN) + MARGIN
        pygame.draw.rect(self.screen, BLUE, (start_x, start_y, CELL_SIZE, CELL_SIZE))
        
        goal_x = self.goal[1] * (CELL_SIZE + MARGIN) + MARGIN
        goal_y = self.goal[0] * (CELL_SIZE + MARGIN) + MARGIN
        pygame.draw.rect(self.screen, GREEN, (goal_x, goal_y, CELL_SIZE, CELL_SIZE))
        
        self.draw_stats()
        
        # Add result message
        result_text = "Path Found!" if path else "No Path Found!"
        result_color = GREEN if path else RED
        text = self.title_font.render(result_text, True, result_color)
        self.screen.blit(text, (GRID_SIZE * (CELL_SIZE + MARGIN) + 20, 
                                WINDOW_HEIGHT - 60))
        
        pygame.display.flip()
        
        # Wait for user to close window
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
