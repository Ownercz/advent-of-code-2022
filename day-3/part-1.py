
def read_input():
    input_path = '/home/ownercz/Seafile/Package/advent-of-code-2022/test_input'
    input_file_content = open(input_path,'r')
    return(input_file_content.read().splitlines())




if __name__ == "__main__":
    print(read_input())