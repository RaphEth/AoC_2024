import re



# --- Day 3: Mull It Over ---


file = "inputs/day3.txt"


def read_file(file):
    """Read the input file and return its content as a single string."""
    with open(file, "r") as f:
        return f.read()


def find_multiplications(content):
    """Extract all mul(x, y) patterns and return a list of lists of values."""
    values = re.findall(r"mul\(\d{1,3},\d{1,3}\)", content)
    return [x.replace("mul(", "").replace(")", "").split(",") for x in values]


def calculate_sum(multiplications):
    """Calculate the sum of products for a list of [x, y] pairs."""
    return sum(int(x) * int(y) for x, y in multiplications)


def extract_sections(content):
    """Separate the 'do' and 'don't' sections from the content."""
    do, dont = [], []

    # Process first section
    if "don't" in content:
        do.append(content[:content.find("don't")])
        content = content[content.find("don't"):]

    # Process the remaining string
    while "do()" in content or "don't()" in content:
        do_index = content.find("do()")
        dont_index = content.find("don't()")

        if dont_index != -1 and (do_index == -1 or dont_index < do_index):
            # Extract a "don't" section
            dont.append(content[dont_index:do_index if do_index != -1 else None])
            content = content[do_index if do_index != -1 else len(content):]
        elif do_index != -1:
            # Extract a "do" section
            do.append(content[do_index:dont_index if dont_index != -1 else None])
            content = content[dont_index if dont_index != -1 else len(content):]

    return do


def part1(file):
    """Calculate Part 1 answer."""
    content = read_file(file)
    multiplications = find_multiplications(content)
    return calculate_sum(multiplications)


def part2(file):
    """Calculate Part 2 answer."""
    content = read_file(file)
    do = extract_sections(content)  # Only process "do" sections
    do_content = " ".join(do)  # Combine all "do" sections into one string
    multiplications = find_multiplications(do_content)
    return calculate_sum(multiplications)


# Run Parts 1 and 2
print(f"Part 1: {part1(file)}")
print(f"Part 2: {part2(file)}")

# My answers
# Part 1: 166905464
# Part 2: 72948684


