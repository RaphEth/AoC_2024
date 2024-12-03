


# --- Day 2: Red-Nosed Reports ---

file = "inputs/Day2.txt"


def check_row(row):
    """Check if the row is safe, i.e. strictly increasing or decreasing by less than 3"""
    increasing_sorted = sorted(row)
    decreasing_sorted = sorted(row, reverse=True)
    is_safe = True
    if row == increasing_sorted or row == decreasing_sorted:
        # is stricly increasing or decreasing
        for i in range(len(row) - 1):
            # check if increasing by less than 3 or not increasing, else skip line
            difference = abs(row[i] - row[i + 1])
            if difference > 3 or difference == 0:
                is_safe = False
                break

    else:
        is_safe = False

    return is_safe

def parse_input(file):
    """Parse the input file, return a list of lists of ints"""
    with open(file, "r") as f:
        return [[int(x) for x in line.strip().split(" ")] for line in f]

def part1(file):
    """Part 1 - Check if the row is safe"""
    safe_reports = 0
    # Parse input
    converted_rows = parse_input(file)

    for row in converted_rows:
        # check if row is safe
        if check_row(row):
            safe_reports += 1

    return safe_reports


def part2(file):
    """Part 2 - Check if removing one element makes the row safe"""
    safe_reports = 0
    # parse input
    converted_rows = parse_input(file)

    # Check each rows
    for row in converted_rows:
        # if not safe, check if removing one element makes it safe
        if not check_row(row):
            # Try each element
            for i in range(len(row)):
                # Create a copy of the row without the ith element
                temp_list = row.copy()
                temp_list.pop(i)
                # Check if it's's safe
                if check_row(temp_list):
                    safe_reports += 1
                    break
        else:
            safe_reports += 1

    return safe_reports


print(f"Part 1: {part1(file)} safe reports")
print(f"Part 2: {part2(file)} safe reports")
