
def bitCheck(value,index):
    temp = value >> (index-1)
    if (temp & 1):
        return 1
    else:
        return 0

def set_bit(value, bit):
    return value | (1<<bit)

def mostCommonCheck(set,pos):

    count = 0
    for v in set:
        #print(v)
        #print(pos)
        if bitCheck(v,pos) == 1:
            count = count + 1
    #print('count', count)
    #print('length',len(set))
    if count >= (len(set)/2):
        return 1
    else:
        return 0

def leastCommonCheck(set,pos):

    count = 0
    for v in set:
        #print(v)
        #print(pos)
        if bitCheck(v,pos) == 1:
            count = count + 1
    #print('count', count)
    #print('length',len(set))
    if count < (len(set)/2):
        return 1
    else:
        return 0

def main():

    array = []
    arrayM = []
    arrayL = []

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D3.txt","r") as f:
        for val in f.read().split():
            array.append(int(val,2)) 

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D3.txt","r") as f:
        firstline = f.readline().rstrip()
        binLen = len(str(firstline))

    arrayM = array
    arrayL = array

    #oxygen part
    for i in range(0,binLen):
        curCriteria = mostCommonCheck(arrayM,binLen-i)
        #print('criteria',curCriteria)
        if curCriteria == 1:
            arrayM = [num for num in arrayM if bitCheck(num,binLen-i) == 1 ]

        elif curCriteria == 0:
            arrayM = [num for num in arrayM if bitCheck(num,binLen-i) == 0 ]
        
        #print(arrayM)
        if len(arrayM) == 1:
            break

    #CO2 part
    for i in range(0,binLen):
        curCriteria = leastCommonCheck(arrayL,binLen-i)
        #print('criteria',curCriteria)
        if curCriteria == 1:
            arrayL = [num for num in arrayL if bitCheck(num,binLen-i) == 1 ]

        elif curCriteria == 0:
            arrayL = [num for num in arrayL if bitCheck(num,binLen-i) == 0 ]
        
        #print(arrayL)
        if len(arrayL) == 1:
            break

    print(arrayM[0]*arrayL[0])

main()