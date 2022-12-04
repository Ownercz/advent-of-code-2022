
def read_input():
    input_path = '/home/ownercz/Seafile/Package/advent-of-code-2022/day-4/input'
    input_file_content = open(input_path,'r')
    return(input_file_content.read().splitlines())

def line_to_set(entry_line):
    ranges = entry_line.split(',')
    elves = []
    print(entry_line)
    for range in ranges:
        range_start = int(range.split('-')[0])
        range_end = int(range.split('-')[1])
        range_final = set()
        while range_start <= range_end:
            range_final.add(range_start)
            range_start = range_start + 1
        elves.append(range_final)
    print(elves)
    return elves

def check_subset(elves):
    if elves[0].issubset(elves[1]): print("yes") ;return 1
    elif elves[1].issubset(elves[0]): print("yes") ;return 1
    else: print("no"); return 0

def sum_count(entry,sum):
    return sum+entry

if __name__ == "__main__":
    sum = 0
    for entry_line in read_input():
        #sum = sum_count(check_subset(line_to_set(entry_line)),sum)
        sum = sum + check_subset(line_to_set(entry_line))
    print(sum)