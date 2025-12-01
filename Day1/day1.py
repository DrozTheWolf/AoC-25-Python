def part1():
    with open("input.txt") as file:
        current_num = 50
        code = 0
        for line in file:
            line = line.strip()
            step = int(line[1:])
            if line[0] == "L":
                current_num -= step
            elif line[0] == "R":
                current_num += step

            current_num %= 100

            if current_num == 0:
                code += 1

            print(f"Current Val: {current_num} \n Code: {code}")

        print("Final Code:", code)


def part2():
    with open("input.txt") as file:
        current_num = 50
        code = 0
        for line in file:
            line = line.strip()
            step = int(line[1:])
            for i in range (0, step):
                if line[0] == "L":
                    current_num -= 1
                elif line[0] == "R":
                    current_num += 1

                current_num %= 100

                if current_num == 0:
                    code += 1
                    print(f"Current step: {line}, incremented one")


        print("Final Code:", code)


if __name__ == '__main__':
    part2()