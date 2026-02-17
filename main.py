"""
AI Pathfinder - Main Application
Implements and visualizes uninformed search algorithms
"""
import sys
from utils.grid_utils import initialize_grid, add_random_walls
from gui.visualizer import PathfindingVisualizer
from algorithms import bfs, dfs, ucs, dls, iddfs, bidirectional_search


def create_test_grid():
    """Create a test grid with random walls"""
    grid = initialize_grid()
    add_random_walls(grid, num_walls=15)
    return grid


def run_algorithm(algorithm_name, grid, start, goal):
    """Run a specific algorithm with visualization"""
    print(f"\n{'='*50}")
    print(f"Running {algorithm_name}")
    print(f"{'='*50}")
    
    # Create visualizer
    visualizer = PathfindingVisualizer(grid.copy(), start, goal, algorithm_name)
    
    # Select and run algorithm
    if algorithm_name == "BFS":
        path, visited = bfs(grid, start, goal, visualizer)
    elif algorithm_name == "DFS":
        path, visited = dfs(grid, start, goal, visualizer)
    elif algorithm_name == "UCS":
        path, visited = ucs(grid, start, goal, visualizer)
    elif algorithm_name == "DLS":
        path, visited = dls(grid, start, goal, depth_limit=25, visualizer=visualizer)
    elif algorithm_name == "IDDFS":
        path, visited = iddfs(grid, start, goal, max_depth=35, visualizer=visualizer)
    elif algorithm_name == "Bidirectional":
        path, visited = bidirectional_search(grid, start, goal, visualizer)
    else:
        print(f"Unknown algorithm: {algorithm_name}")
        return
    
    # Show result
    visualizer.show_result(path, visited)
    
    # Print results
    if path:
        print(f"✓ Path found!")
        print(f"  Path length: {len(path)}")
        print(f"  Nodes explored: {len(visited)}")
    else:
        print(f"✗ No path found")
        print(f"  Nodes explored: {len(visited)}")


def main():
    """Main application entry point"""
    print("="*50)
    print("AI PATHFINDER - Uninformed Search Visualization")
    print("="*50)
    
    # Define start and goal positions
    start = (1, 1)
    goal = (13, 13)
    
    # Create grid
    grid = create_test_grid()
    
    # Ensure start and goal are not walls
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0
    
    # List of algorithms
    algorithms = ["BFS", "DFS", "UCS", "DLS", "IDDFS", "Bidirectional"]
    
    print("\nAvailable Algorithms:")
    for i, algo in enumerate(algorithms, 1):
        print(f"{i}. {algo}")
    print("0. Run all algorithms")
    print("q. Quit")
    
    while True:
        choice = input("\nSelect algorithm (0-6 or q): ").strip()
        
        if choice.lower() == 'q':
            print("Exiting...")
            break
        
        try:
            if choice == '0':
                # Run all algorithms
                for algo in algorithms:
                    run_algorithm(algo, grid, start, goal)
            else:
                idx = int(choice) - 1
                if 0 <= idx < len(algorithms):
                    run_algorithm(algorithms[idx], grid, start, goal)
                else:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Exiting...")
            break


if __name__ == "__main__":
    main()
