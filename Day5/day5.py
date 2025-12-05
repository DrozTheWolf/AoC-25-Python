ranges = []
ids = []

def load_file():
    global ranges
    global ids
    with open("input.txt") as file:
        file_data = file.read()
        parts = file_data.split(("\n\n"))

        for line in parts[0].split("\n"):
            range = line.strip().split("-")
            ranges.append((int(range[0]),int(range[1])))
        for line in parts[1].split("\n"):
            ids.append(int(line.strip()))


def part1():
    load_file()
    fresh_id_num = 0

    for id in ids:
        for min,max in ranges:
            if min <= id <= max:
                fresh_id_num += 1
                break

    print(fresh_id_num)

def part2():
    load_file()
    fresh_id_num = 0

    merge_ranges()

    for range in ranges:
        fresh_id_num += (range[1] - range[0]) + 1
        # Needs +1 to be inclusive
    print(fresh_id_num)

def merge_ranges():
    global ranges
    merge_list = []
    # Sort them by start num
    ranges = sorted(ranges, key=lambda x : x[0])

    for range in ranges:
        if not merge_list or range[0] > merge_list[-1][1]:
            merge_list.append((range[0], range[1]))
        else:
            merge_list[-1] = (merge_list[-1][0], max(merge_list[-1][1], range[1]))

    ranges = merge_list

    for range in ranges:
        print(range)


    return

if __name__ == '__main__':
    part2()