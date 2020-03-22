import random
all = []
lines_counter = 0
with open('medium.txt', 'r') as file:
    for f in file:
        all.append(f.split())
        lines_counter +=1

#dla n=4, rozwiązań jest tyle co w sumie pozycji z czwartego rzędu
#dla very_easy=16, dla easy= 16382, dla medium=1.584563250285286e+29
desire = []
while len(desire) != 160:
    row_counter = 0
    current_road = ''
    while row_counter < lines_counter:
        if row_counter ==0:
            pos_counter = 0
            current_road += all[row_counter][pos_counter]
            row_counter += 1
        else:
            pos_counter += random.randint(0,1)
            current_road += all[row_counter][pos_counter]
            row_counter +=1
    if current_road not in desire:
        desire.append(current_road)

def split(word):
    return [char for char in word]
final_dict= {}
for x in desire:
    y = split(x)
    number = 0
    for char in y:
        number += int(char)
    final_dict[x]=number

print({k: v for k, v in sorted(final_dict.items(), key=lambda item: item[1])})
