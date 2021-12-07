import time

def p2Cost(dif):
    sum = dif*(dif+1)/2
    return sum

def main():
    startTime = time.time()


    sum = 0
    arrayInput = []
    arrayInputTest = [16,1,2,0,4,2,7,1,2,14]

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D7.txt","r") as f:
        for val in f.read().split(','):
            arrayInput.append(int(val))

    #calculates average of all values
    for val in arrayInput:
        sum = sum + val

    avg = sum/len(arrayInput)

    minFound = 0
    fuelCost = [0]*max(arrayInput)
    minFound = 0
    pos = int(avg)

    while minFound == 0:
        
        if fuelCost[pos] == 0:
            for val in arrayInput:
                fuelCost[pos] += p2Cost(abs(val-pos))
        if fuelCost[pos+1] == 0:
            for val in arrayInput:
                fuelCost[pos+1] += p2Cost(abs(val-(pos+1)))
        if fuelCost[pos-1] == 0:
            for val in arrayInput:
                fuelCost[pos-1] += p2Cost(abs(val-(pos-1)))

        if fuelCost[pos] < fuelCost[pos+1] and fuelCost[pos] < fuelCost[pos-1]:
            minFound = 1

        elif fuelCost[pos] > fuelCost[pos-1]:
            pos -= 1
        elif fuelCost[pos] > fuelCost[pos+1]:
            pos += 1

    print(pos,fuelCost[pos])
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
        

main()



