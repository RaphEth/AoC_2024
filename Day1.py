

# --- Day 1: Historian Hysteria ---


# open file
file = "inputs/Day1.txt"

def part1(file):
    """Part 1: Calculate the sum of the distances between the two lists"""
    # read file and store in lists
    left_list = []
    right_list = []

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            pair = line.split("   ")
            # convert to int
            ordered_pair = [int(x) for x in pair]

            # add to respective lists
            left_list.append(ordered_pair[0])
            right_list.append(ordered_pair[1])

    # pair up and perfom distance calculations
    left_list.sort()
    right_list.sort()
    distances = [abs(left_list[i] - right_list[i]) for i in range(len(left_list))]

    # return the sum of the distances
    return sum(distances)


def part2(file):
    """Part 2: Calculate the sum of the simliarity scores"""
    # read file and store in lists
    left_list = []
    right_list = []

    # create a dict with each num for the left list with value = 0
    num_dict = {}

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            pair = line.split("   ")
            # convert to int
            ordered_pair = [int(x) for x in pair]

            # add to respective lists
            left_list.append(ordered_pair[0])
            right_list.append(ordered_pair[1])

    for num in left_list:
        # get the number of instances of the num in the list
        instance_count = right_list.count(num)
        num_dict[num] = instance_count * num + num_dict.get(num, 0)

    return sum(num_dict.values())


print(f"Part 1: {part1(file)}")
print(f"Part 2: {part2(file)}")




