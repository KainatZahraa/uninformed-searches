
# AI Pathfinder - Uninformed Search Visualization

A comprehensive implementation and visualization of six uninformed search algorithms for pathfinding in a grid environment. This project demonstrates how different "blind" search strategies explore a map from a Start Point to a Target Point while avoiding static obstacles.

## 🎯 Project Overview

This project implements and visualizes six fundamental uninformed search algorithms:
1. **Breadth-First Search (BFS)**
2. **Depth-First Search (DFS)**
3. **Uniform-Cost Search (UCS)**
4. **Depth-Limited Search (DLS)**
5. **Iterative Deepening DFS (IDDFS)**
6. **Bidirectional Search**

## ✨ Features

- **Real-time Visualization**: Watch algorithms explore the grid step-by-step
- **Interactive GUI**: Built with Pygame for smooth visualization
- **Color-coded States**: 
  - 🔵 Blue = Start Position
  - 🟢 Green = Goal Position
  - ⬛ Black = Walls/Obstacles
  - 🔶 Cyan = Visited Nodes
  - 🟡 Yellow = Frontier Nodes
  - 🟠 Orange = Current Node
  - 🟣 Purple = Final Path
- **Performance Metrics**: Track nodes explored and path length for each algorithm
- **Multiple Test Cases**: Run individual algorithms or all at once

## 📋 Requirements

```
Python 3.8+
pygame 2.6.0+
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI_A1_23F-XXXX.git
   cd AI_A1_23F-XXXX
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

## 💻 Usage

Run the main application:
```bash
python main.py
```

### Menu Options:
```
1. BFS - Breadth-First Search
2. DFS - Depth-First Search
3. UCS - Uniform-Cost Search
4. DLS - Depth-Limited Search
5. IDDFS - Iterative Deepening DFS
6. Bidirectional - Bidirectional Search
0. Run all algorithms
q. Quit
```

Enter the number corresponding to the algorithm you want to visualize.

## 📁 Project Structure

```
AI_A1_23F-XXXX/
│
├── algorithms/           # Algorithm implementations
│   ├── __init__.py
│   ├── bfs.py           # Breadth-First Search
│   ├── dfs.py           # Depth-First Search
│   ├── ucs.py           # Uniform-Cost Search
│   ├── dls.py           # Depth-Limited Search
│   ├── iddfs.py         # Iterative Deepening DFS
│   └── bidirectional.py # Bidirectional Search
│
├── gui/                  # Visualization components
│   ├── __init__.py
│   └── visualizer.py    # Pygame GUI implementation
│
├── utils/                # Utility functions
│   ├── __init__.py
│   └── grid_utils.py    # Grid operations and Node class
│
├── config.py            # Configuration settings
├── main.py              # Main application entry point
├── test_algorithms.py   # Algorithm testing
└── README.md            # This file
```

## 🎮 How It Works

### Movement Order
As per assignment requirements, the algorithms explore neighbors in this specific clockwise order:
1. Up
2. Right
3. Down
4. Bottom-Right (Diagonal)
5. Left
6. Top-Left (Diagonal)

### Grid Configuration
- **Grid Size**: 15x15
- **Cell Size**: 30 pixels
- **Random Obstacles**: 15 walls per grid
- **Start Position**: (1, 1) - Top-left area
- **Goal Position**: (13, 13) - Bottom-right area

### Algorithm Behavior

#### BFS (Breadth-First Search)
- Uses a queue (FIFO)
- Explores level by level
- Guarantees shortest path in unweighted graphs
- Complete and optimal

#### DFS (Depth-First Search)
- Uses a stack (LIFO)
- Explores as deep as possible first
- Memory efficient
- Not guaranteed to find shortest path

#### UCS (Uniform-Cost Search)
- Uses a priority queue based on path cost
- Considers diagonal movement cost (√2 ≈ 1.414)
- Guarantees optimal path with weighted edges
- Expands lowest-cost nodes first

#### DLS (Depth-Limited Search)
- DFS with a maximum depth limit (40)
- Prevents infinite loops in deep/infinite graphs
- May not find solution if depth limit is too small

#### IDDFS (Iterative Deepening DFS)
- Combines benefits of BFS and DFS
- Iteratively increases depth limit
- Complete like BFS, memory efficient like DFS
- Max depth: 50

#### Bidirectional Search
- Searches from both start and goal simultaneously
- Meets in the middle
- Reduces search space significantly
- Can be faster than unidirectional search

## 🎨 Configuration

Edit `config.py` to customize:
- Grid size and cell dimensions
- Colors for visualization
- Animation speed (ANIMATION_DELAY)
- Movement costs

## 📊 Performance Comparison

| Algorithm | Completeness | Optimality | Time Complexity | Space Complexity |
|-----------|-------------|------------|-----------------|------------------|
| BFS | ✅ Yes | ✅ Yes | O(b^d) | O(b^d) |
| DFS | ⚠️ No* | ❌ No | O(b^m) | O(bm) |
| UCS | ✅ Yes | ✅ Yes | O(b^(C*/ε)) | O(b^(C*/ε)) |
| DLS | ⚠️ No | ❌ No | O(b^l) | O(bl) |
| IDDFS | ✅ Yes | ✅ Yes | O(b^d) | O(bd) |
| Bidirectional | ✅ Yes | ✅ Yes | O(b^(d/2)) | O(b^(d/2)) |

*b = branching factor, d = depth of solution, m = maximum depth, l = depth limit

## 🐛 Known Limitations

- DLS may fail if the depth limit is too restrictive
- IDDFS can be slow due to repeated exploration at each depth level
- Grid is regenerated randomly each run (obstacles change)

## 🤝 Contributing

This is an academic project for AI 2002 - Artificial Intelligence (Spring 2026). 



---

**Note**: Replace XXXX with your actual student ID and update personal information before submission.
