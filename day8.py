import re
from collections import defaultdict
import math

# Part A set to True, Part B set to False
factor_harmonics = True

grid = []
with open("inputs/day8.txt") as f:
    grid = [line.strip() for line in f.readlines()]

def dist_points(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    return dy / dx if dx != 0 else None

def is_point_antinode(orig_p, p1, p2):
    dist_1 = dist_points(orig_p, p1)
    dist_2 = dist_points(orig_p, p2)
    
    if factor_harmonics:
        # Ensure the distances satisfy the antinode condition
        if not (math.isclose(dist_1, 2 * dist_2, rel_tol=1e-9)):
            return False
    
    # Check if slopes match for line of sight
    slope1 = slope(orig_p, p1)
    slope2 = slope(p1, p2)
    return slope1 == slope2

def print_scene(grid):
    for i, line in enumerate(grid):
        print(line + " " + str(i))

# Extract all antennas
antennas = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if re.match(r"[a-zA-Z0-9]", grid[i][j]):  # Match alphanumeric characters
            antennas[grid[i][j]].append((i, j))

# Check for antinodes for all grid points
antinodes = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        orig_p = (i, j)
        for char, positions in antennas.items():
            for p1 in positions:
                for p2 in positions:
                    # Ensure p1 and p2 have the same character
                    if p1 != p2 and grid[p1[0]][p1[1]] == grid[p2[0]][p2[1]]:
                        if is_point_antinode(orig_p, p1, p2):
                            antinodes.append(orig_p)

unique_antinodes = list(set(antinodes))

# Print the results
print("Grid:")
print_scene(grid)
print("\nAntenna positions:")
for char, pos_list in antennas.items():
    print(f"{char}: {pos_list}")


grid_with_antinodes = [list(row) for row in grid]


for antinode in unique_antinodes:
    orig_p = antinode
    grid_with_antinodes[orig_p[0]][orig_p[1]] = '#'

grid_with_antinodes = [''.join(row) for row in grid_with_antinodes]



print("\nGrid with antinodes marked as #:")
print_scene(grid_with_antinodes)


print("\nAntinodes:")
for antinode in unique_antinodes:
    print(antinode)

print(f"Total count: {len(unique_antinodes)}")
