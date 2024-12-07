grid = []
with open("inputs/day7.txt") as f:
    grid = f.readlines()
    grid = [line.replace("\n", "") for line in grid]

def print_scene(grid):
    for i, line in enumerate(grid):
        print( line + " " + str(i))

print_scene(grid)

class Guard:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
        pass
    
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
        match self.dir:
            case "up":
                pass

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
        for j in range(len(grid)):
            direction = Guard.dir_sym2str(grid[i][j])
            if direction != None:
                return (i,j, direction)

print(find_guard(grid))
