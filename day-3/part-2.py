import string

def read_input():
    input_path = '/home/ownercz/Seafile/Package/advent-of-code-2022/day-3/input'
    input_file_content = open(input_path,'r')
    return(input_file_content.read().splitlines())

def compare_inventory(first,second):
    common_first = {}
    common_second = {}
    intersection = {}

    for inv_item in first:
        common_first[inv_item] = common_first.get(inv_item, 0) + 1
    for inv_item in second:
        common_second[inv_item] = common_second.get(inv_item, 0) + 1

    for key in common_first:
        if key in common_second:
            sum = common_first[key]+common_second[key]
            intersection[key] = intersection.get(sum,0) + sum

    return(intersection)

def priority_count():
    index = 1
    priority_dict = {}

    for single_char in list(string.ascii_lowercase):
        priority_dict[single_char] = index
        index = index + 1

    for single_char in list(string.ascii_uppercase):
        priority_dict[single_char] = index
        index = index + 1

    return priority_dict

def points(valued_chars, entry_line ):
    sum = 0
    if len(entry_line) == 0:
        return 0
    for key in entry_line:
        sum = sum + (valued_chars[key])
    return sum

def group_elves(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def find_common(group):
    for char in group[0]:
        if char in group[1]:
            if char in group[2]:
                return char

if __name__ == "__main__":
    combined = {}
    summary = 0

    groups = list(group_elves(read_input(), 3))
    for group in groups:
        summary = summary + (points(priority_count(),find_common(group)))
    print(summary)