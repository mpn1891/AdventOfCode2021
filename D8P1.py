
inputArray = []
segArray = []
outArray = []
total = 0
wrkArray = []

with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D8.txt","r") as f:
    items = f.read().split('\n')
    for item in items:
        inputArray.append(str(item))

    for i in range(len(inputArray)):
        inputArray[i] = inputArray[i].split()
        segArray.append(inputArray[i][:10])
        outArray.append(inputArray[i][11:])

    for j in range(len(outArray)):
        for val in outArray[j]:
            if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
                total += 1


    print(total)





