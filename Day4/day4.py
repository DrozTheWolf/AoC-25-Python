deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

grid = []
rows = 0
cols = 0
num_to_remove = 1 #Start at 1 so while loop runs
coords_to_remove = []

def load_grid():
    global grid

    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file]
        # Cool ass way of parsing the input, thanks Python
    global rows
    global cols
    rows = len(grid)
    cols = len(grid[0])

def part1():
    load_grid()
    final_num = 0

    for y in range(rows):
        for x in range(cols):
            # print(f"For Index {j},{i}, value is {grid[i][j]}")
            if grid[y][x] == "@":
                if check_index(x, y):
                    final_num += 1

    print(f"Final Num: {final_num}")

def part2():
    load_grid()
    final_num = 0
    global num_to_remove
    global coords_to_remove
    while num_to_remove > 0:
        coords_to_remove = []
        num_to_remove = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "@":
                    if check_index(x, y):
                        num_to_remove += 1
                        final_num += 1
                        coords_to_remove.append((x,y))
        print(f"Removing {num_to_remove} rolls!")
        remove_rolls()
    print(f"Removed a total of {final_num}")


def remove_rolls():
    global grid
    for rx,ry in coords_to_remove:
        grid[ry][rx] = "."

def check_index(x, y):
    num_of_rolls = 0
    for dX,dY in deltas:
        nX, nY = dX + x, dY + y
        try:
            if 0 <= nY < rows and 0 <= nX <= cols:
                if grid[nY][nX] == "@":
                    num_of_rolls += 1
        except IndexError:
            pass
    print(f"For item {x},{y}, found {num_of_rolls} rolls")
    if num_of_rolls < 4:
        print(f"Found A Suitable Roll: {x},{y}")
        return True
    return False

if __name__ == '__main__':
    part2()