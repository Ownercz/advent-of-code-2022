def read_input():
    input_path = '/home/ownercz/Seafile/Package/advent-of-code-2022/day-6/input'
    input_file_content = open(input_path,'r')
    return(input_file_content.read().splitlines())

def process_start(line):
    position = 0
    four_chars = []
    print(position)
    print(line)
    while position != len(line):
        four_chars.append(line[position])
        if len(four_chars) > 4: four_chars.pop(0)
        if len(set(four_chars)) == len(four_chars) and len(four_chars) == 4:
            print(four_chars)
            return position
        position = position + 1

def message_marker(line):
    position = 0
    four_chars = []
    print(position)
    print(line)
    while position != len(line):
        four_chars.append(line[position])
        if len(four_chars) > 14: four_chars.pop(0)
        if len(set(four_chars)) == len(four_chars) and len(four_chars) == 14:
            print(four_chars)
            return position
        position = position + 1

if __name__ == "__main__":
    for line in read_input():
        print(message_marker(line)+1)
