import re




def read_input():
    input_path = '/home/ownercz/Seafile/Package/advent-of-code-2022/day-5/input'
    input_file_content = open(input_path,'r')
    return(input_file_content.read().splitlines())

def move_crane_command(regex, line):
    move_result = {}
    matches = re.finditer(regex, line, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        move_result["move"] = (match.group(1))
        move_result["from"] = (match.group(2))
        move_result["to"] = (match.group(3))
    if len(move_result) > 0:    return move_result
    else: print("LINE " + line) ;exit(1);return None

def process_move_crane(command,cranes):
    if command != None:
        print(cranes)
        move_crane = int(command["move"])
        from_crane = int(command["from"])-1
        to_crane = int(command["to"])-1
        print("Will move times:" + str(move_crane))
        while move_crane > 0:
            print("Will move times:" + str(move_crane))
            print("Will move from: "+str(from_crane) + str(cranes[from_crane]))
            print("Will move to: " + str(to_crane) + str(cranes[to_crane]))
            if len(cranes[from_crane]) > 0:
                moved = cranes[from_crane].pop()
                print("Moving...." + str(moved))
                print("Crane has been lifted: ")
                print(cranes[from_crane])
                print("Crane is setting elsewhere:" )
                print(cranes[to_crane])
                cranes[to_crane].append(moved)
                print(cranes[to_crane])
                print("Step done!")
            else:
                print("NOT enough items!!!")
                print(cranes)
                exit(1)
            move_crane = move_crane -1
    else: print("Nothing was moved.")
    return cranes
if __name__ == "__main__":
    regex = r"move\ (\d+)\ from\ (\d)\ to\ (\d)"
    crane = []
    crane.append(["W","B","D","N","C","F","J"])
    crane.append(["P","Z","V","Q","L","S","T"])
    crane.append(["P","Z","B","G","J","T"])
    crane.append(["D","T","L","J","Z","B","H","C"])
    crane.append(["G","V","B","J","S"])
    crane.append(["P","S","Q"])
    crane.append(["B","V","D","F","L","M","P","N"])
    crane.append(["P","S","M","F","B","D","L","R"])
    crane.append(["V","D","T","R"])
    #print(crane)

    #crane = []
    #crane.append(["Z","N"])
    #crane.append(["M","C","D"])
    #crane.append(["P"])

    for line in read_input():
        crane = process_move_crane(move_crane_command(regex, line), crane)
    print(crane)
    for crane_entry in crane:
        if len(crane_entry) > 0:
            print(crane_entry[-1])
