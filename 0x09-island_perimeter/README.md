# 0x09. Island Perimeter

**Weight**: 1  
**Project Start**: May 6, 2024, 4:00 AM  
**Deadline**: May 10, 2024, 4:00 AM  
**Checker Release**: May 7, 2024, 4:00 AM  
**Auto Review Deadline**: At the project deadline  

## Overview
In the "0. Island Perimeter" project, you'll utilize your skills in algorithms, data structures (particularly 2D arrays or matrices), and conditional logic to solve a geometric problem set in a grid context. The main objective is to calculate the perimeter of a single island represented within a 2D array of integers. Mastery over navigating and analyzing 2D arrays and applying logical conditions to determine the perimeter of the island is essential.

## Concepts Needed
- **2D Arrays (Matrices)**:
  - Access and iterate over elements.
  - Navigate through adjacent cells horizontally and vertically.
- **Conditional Logic**:
  - Apply conditions to determine a cell's contribution to the island's perimeter.
- **Counting Techniques**:
  - Develop methods to count edges contributing to the perimeter.
- **Problem-Solving Strategies**:
  - Break down the task into smaller units, such as identifying land cells and their perimeter contributions.
- **Python Programming**:
  - Implement nested loops for iterating over grid cells.
  - Use conditional statements to assess adjacent cell status.

## Resources
- [Python Official Documentation](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- [GeeksforGeeks: Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/multi-dimensional-lists-in-python/)
- [TutorialsPoint: Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- YouTube Tutorials on Python 2D arrays and lists

## Requirements
- **Environment**: Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **Editors**: vi, vim, emacs
- **Code Style**: PEP 8 style (version 1.7)
- **Documentation**: Must include a `README.md` file and inline comments/documentation for modules and functions
- **Execution**: All files must be executable and should start with `#!/usr/bin/python3`
- **Restrictions**: No external modules are allowed to be imported

## Task: Island Perimeter
**Function Prototype**: `def island_perimeter(grid):`
- **Input**:
  - `grid`: a list of lists of integers where `0` represents water and `1` represents land.
  - Each cell has a side length of 1.
  - Cells are connected horizontally or vertically.
  - The grid is rectangular, fully surrounded by water, and its dimensions do not exceed 100x100.
  - Contains only one contiguous island without any enclosed lakes.
- **Output**:
  - Returns the perimeter of the island described in the grid.

**Example Execution**:
```bash
#!/usr/bin/python3
"""
Main file for testing
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12

