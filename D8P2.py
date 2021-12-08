import time

def charStrip(char,string):
    return string.replace(char,'')

def sortChars(string):
    
    temp = sorted(string)
    return "".join(temp)



def main():

    startTime = time.time()


    inputArray = []
    segArray = []
    outArray = []
    total = ''
    fiveSpot = []
    sixSpot = []
    answer = 0
    totalArray = []

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D8.txt","r") as f:
        items = f.read().split('\n')
        for item in items:
            inputArray.append(str(item))

        for i in range(len(inputArray)):
            inputArray[i] = inputArray[i].split()
            segArray.append(inputArray[i][:10])
            outArray.append(inputArray[i][11:])

        for j in range(len(segArray)):
            wrkArray = [0,0,0,0,0,0,0,0,0,0]
            fiveSpot.clear()
            sixSpot.clear()
            total = ''
            for k in range(len(segArray[j])):
            
                #finds the easy ones by len and grabs the pos of the 5 and 6's for future
                if len(segArray[j][k]) == 2:
                    wrkArray[1] = sortChars(segArray[j][k])
            
                elif len(segArray[j][k]) == 3:
                    wrkArray[7] = sortChars(segArray[j][k])

                elif len(segArray[j][k]) == 4:
                    wrkArray[4] = sortChars(segArray[j][k])

                elif len(segArray[j][k]) == 5:
                    fiveSpot.append(k)

                elif len(segArray[j][k]) == 6:
                    sixSpot.append(k)
    
                elif len(segArray[j][k]) == 7:
                    wrkArray[8] = sortChars(segArray[j][k])

            #gets top character by 7 - 1
            first_set = set(wrkArray[7])
            second_set = set(wrkArray[1])
            top = first_set.difference(second_set)
            topStr = ', '.join(top)
            #print(topStr)

            #print(top)
            #print(fiveSpot)

            #finds 3 by matching both of the 1 values to a len(5)
            for val in fiveSpot:
                if wrkArray[1][0] in segArray[j][val] and wrkArray[1][1] in segArray[j][val]:
                    wrkArray[3] = sortChars(segArray[j][val])
                    fiveSpot.remove(val)

            #gets bottom from (3-(top+4))
            temp = sortChars(topStr+wrkArray[4])

            bottom = wrkArray[3]
            for char in temp:
                bottom = charStrip(char,bottom)

            #gets middle from (3-(top+1+bottom))
            middle = wrkArray[3]
            temp = sortChars(topStr+wrkArray[1] + bottom)
            for char in temp:
                middle = charStrip(char,middle)

           
            # gets 0 from whichever len6 is missing middle
            for z in sixSpot:
                if middle not in segArray[j][z]:
                    wrkArray[0] = sortChars(segArray[j][z])
                    sixSpot.remove(z)

            #gets 9 from 4 + top + bottom
            wrkArray[9] =  sortChars(wrkArray[4] + topStr + bottom)

            #last len6 spot is 6
            for z in sixSpot:
                if wrkArray[9] in sortChars(segArray[j][z]):
                    sixSpot.remove(z)
            wrkArray[6] = sortChars(segArray[j][sixSpot[0]])

            #gets top right from 9-6
            topRight = wrkArray[9]
            for char in wrkArray[6]:
                topRight = charStrip(char,topRight)

            #gets 2 from a len5 with topright check
            for val in fiveSpot:
                if topRight in segArray[j][val]:
                    wrkArray[2] = sortChars(segArray[j][val])
                    fiveSpot.remove(val)

            #last len5 is 5
            wrkArray[5] = sortChars(segArray[j][fiveSpot[0]])
                  

            for i in range(len(outArray[j])):
                outArray[j][i] = sortChars(outArray[j][i])

            for i in outArray[j]:
                for j in range(len(wrkArray)):
                    if i == wrkArray[j]:
                        total += str(j)


            totalArray.append(total)

    for x in totalArray:
        answer += int(x)

    print(answer)
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


        


main()





