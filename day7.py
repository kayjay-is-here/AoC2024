grid = []
with open("inputs/day7.txt") as f:
    grid = f.readlines()
    grid = [line.replace("\n", "") for line in grid]

def print_scene(grid):
    for i, line in enumerate(grid):
        print(line + " " + str(i))

print_scene(grid)

class Guard:
    def __init__(self, pos, dir, grid):
        self.pos = pos  # (row, col)
        self.dir = dir  
        self.grid = grid
        self.hit_counter = 0
        self.visited_positions = set()
        self.visited_positions.add(pos)  # Start position is visited

    # Rotates 90 degrees clockwise
    def rotate(self):
        match self.dir:
            case "up":
                self.dir = "right"
            case "right":
                self.dir = "down"
            case "down":
                self.dir = "left"
            case "left":
                self.dir = "up"

    def move_forward(self):
        row, col = self.pos

        match self.dir:
            case "up":
                new_pos = (row - 1, col)
            case "down":
                new_pos = (row + 1, col)
            case "left":
                new_pos = (row, col - 1)
            case "right":
                new_pos = (row, col + 1)

        # Check for collisions
        new_row, new_col = new_pos
        if new_row < 0 or new_row >= len(self.grid) or new_col < 0 or new_col >= len(self.grid[0]):
            print(f"Guard hit out of bounds at {new_pos}. Simulation ending.")
            print_scene(self.grid)
            print(f"Total collisions: {self.hit_counter}")
            print(f"Unique positions visited: {len(self.visited_positions)}")
            exit()  # End simulation if out of bounds
        elif self.grid[new_row][new_col] != '.':
            print(f"Guard hit something at {new_pos}")
            self.hit_counter += 1
            prev_dir = self.dir
            self.rotate()
            print(f"old: {prev_dir} -> new: {self.dir}")
            #print_scene(self.grid)
        else:
            # Update grid: clear old position and set new position
            self.grid[row] = self.grid[row][:col] + '.' + self.grid[row][col+1:]
            self.grid[new_row] = self.grid[new_row][:new_col] + Guard.dir_str2sym(self.dir) + self.grid[new_row][new_col+1:]
            self.pos = new_pos
            self.visited_positions.add(new_pos)  # Mark the new position as visited

    @staticmethod
    def dir_sym2str(char):
        match char:
            case "^":
                return "up"
            case ">":
                return "right"
            case "<":
                return "left"
            case "v":
                return "down"
            case _:
                return None

    @staticmethod
    def dir_str2sym(sym):
        match sym:
            case "up":
                return "^"
            case "right":
                return ">"
            case "left":
                return "<"
            case "down":
                return "v"
            case _:
                return None

def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            direction = Guard.dir_sym2str(grid[i][j])
            if direction is not None:
                return (i, j, direction)

guard_info = find_guard(grid)
if guard_info:
    guard = Guard((guard_info[0], guard_info[1]), guard_info[2], grid)

while True:  # Continue until the simulation is ended by an out-of-bounds hit
    guard.move_forward()
