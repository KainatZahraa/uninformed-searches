"""
Quick test script to verify all algorithms work
"""
from utils.grid_utils import initialize_grid
from algorithms import bfs, dfs, ucs, dls, iddfs, bidirectional_search


def test_algorithm(algo_func, name, grid, start, goal):
    """Test a single algorithm"""
    print(f"\nTesting {name}...", end=" ")
    try:
        path, visited = algo_func(grid, start, goal)
        if path:
            print(f"✓ Path found! Length: {len(path)}, Explored: {len(visited)}")
        else:
            print(f"✗ No path found. Explored: {len(visited)}")
        return True
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False


def main():
    """Run basic tests"""
    print("="*60)
    print("AI Pathfinder - Algorithm Tests")
    print("="*60)
    
    # Create simple grid
    grid = initialize_grid()
    start = (0, 0)
    goal = (10, 10)
    
    # Add a simple wall
    for i in range(5, 15):
        grid[i][5] = 1
    
    # Ensure start and goal are clear
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0
    
    # Test all algorithms
    algorithms = [
        (bfs, "BFS"),
        (dfs, "DFS"),
        (ucs, "UCS"),
        (lambda g, s, gl: dls(g, s, gl, depth_limit=20), "DLS"),
        (lambda g, s, gl: iddfs(g, s, gl, max_depth=25), "IDDFS"),
        (bidirectional_search, "Bidirectional"),
    ]
    
    results = []
    for algo_func, name in algorithms:
        result = test_algorithm(algo_func, name, grid, start, goal)
        results.append((name, result))
    
    print("\n" + "="*60)
    print("Test Summary:")
    print("="*60)
    passed = sum(1 for _, result in results if result)
    print(f"Passed: {passed}/{len(results)}")
    
    for name, result in results:
        status = "✓" if result else "✗"
        print(f"{status} {name}")
    
    print("\nAll tests completed!")


if __name__ == "__main__":
    main()
