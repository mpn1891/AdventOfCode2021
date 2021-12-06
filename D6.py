def main():
    total = 0
    arrayInput = []
    arrayFish = [0,0,0,0,0,0,0,0,0]

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D6.txt","r") as f:
        for val in f.read().split(','):
            arrayInput.append(int(val))

    #Builds base array to start working with
    for x in arrayInput:
        arrayFish[x] += 1
    #iterates through the days 
    for i in range(1,257):
        newFish = arrayFish[0]
        arrayFish.pop(0)
        arrayFish.append(newFish)
        arrayFish[6] += newFish

    #counts total of fish in the array
    for j in range(len(arrayFish)):
        total += arrayFish[j]

    print(total)

main()




