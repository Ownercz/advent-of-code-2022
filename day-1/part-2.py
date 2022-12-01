input_path = 'input'
input_file_content = open(input_path,'r')
input_content = input_file_content.read().splitlines()

calories_sum = []
single = 0
final = len(input_content)-1

for entry in input_content:
    if entry != '':
        single = single + int(entry)
    else:
        calories_sum.append(single)
        single = 0
    if(input_content.index(entry)==final):
        calories_sum.append(single)

calories_sum.sort()
calories_top_three = calories_sum[-3::1]
elf_sum = 0
for elf in calories_top_three:
    elf_sum = elf_sum + elf
print(elf_sum)