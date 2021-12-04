
def bitCheck(value,index):
    if index == 12:
        print(value)
            
    return (value & (1 << index)) != 0

def set_bit(value, bit):
    return value | (1<<bit)


array = []
answer = []
bitTracker = 0




with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D3_test.txt","r") as f:
    firstline = f.readline().rstrip()
    binLen = len(firstline)
    for val in f.read().split():
        array.append(int(val,2))  


for i in range(0,binLen):
    count = 0
    for j in array:
        if bitCheck(j,i):
            count = count + 1
    print(count)
    if count > (len(array)/2):
        bitTracker = set_bit(bitTracker,i)

print(bin(bitTracker))



inverse = bitTracker ^ (2 ** (binLen) - 1)

print(bin(inverse))


gamma = bitTracker

epsilon = inverse
answer = gamma * epsilon
print(answer)
        
           

    





