

array = []
answer = 0
windowA = 0
windowB = 0
with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D1.txt","r") as f:
    for val in f.read().split():
        array.append(int(val))  
        

for i in range(len(array)-3):
    windowA = array[i] + array[i+1] + array[i+2]
    windowB = array[i+1] + array[i+2] + array[i+3]

    if windowB > windowA:
        answer =+ answer + 1


print (answer)