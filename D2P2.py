

array = []
x = 0
y = 0
aim = 0
answer = 0
windowA = 0
windowB = 0
with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D2.txt","r") as f:
    for val in f.read().split():
        array.append(str(val))  
        
print(array)
for i in range(len(array)):
    if array[i] == 'forward':
        x = x + int(array[i+1])
        y = y + (aim*int(array[i+1]))
    elif array[i] == 'up':
        aim = aim - int(array[i+1])
    elif array[i] == 'down':
        aim = aim + int(array[i+1])

print(x,y)

answer = x*y


print (answer)

