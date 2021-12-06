

def main():

    totalOverlap = 0
    arrayS = []
    arrayE = []
    overlapGrid = []
    rows, cols = (1000,1000)

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D5_1.txt","r") as f:
        for line in f.readlines():
            line = line.rstrip()
            arrayS.append(line.split(','))  

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D5_2.txt","r") as f:
        for line in f.readlines():
            line = line.rstrip()
            arrayE.append(line.split(','))  


    #create hit grid
    overlapGrid = [[0 for i in range(cols)] for j in range(rows)]
    
    #print(overlapGrid)
    #check if lines are straight
    #if straight add them to the hit grid

    for i in range(len(arrayS)):
        h = False
        v = False
        #h
        if arrayS[i][1] == arrayE[i][1]: 
            h = True
            #print ('h:',arrayS[i],arrayE[i])
        #v
        if arrayS[i][0] == arrayE[i][0]:
            v = True
            #print ('v:',arrayS[i],arrayE[i])

        xStart = int(arrayS[i][0])
        xEnd = int(arrayE[i][0])
        yStart = int(arrayS[i][1])
        yEnd = int(arrayE[i][1])

        if h == True:
            if xStart < xEnd:
                for k in range(xStart, xEnd+1):
                    overlapGrid[yStart][k] = overlapGrid[yStart][k] + 1
            else:
                for k in range(xEnd, xStart+1):
                    overlapGrid[yStart][k] = overlapGrid[yStart][k] + 1

        if v == True:
            if yStart < yEnd:
                for k in range(yStart, yEnd+1):
                    overlapGrid[k][xStart] = overlapGrid[k][xStart] + 1
            else:
                for k in range(yEnd, yStart+1):
                    overlapGrid[k][xStart] = overlapGrid[k][xStart] + 1
     
    #count hits greater than 1
    for row in overlapGrid:   
        for val in row:
            if val > 1:
                totalOverlap = totalOverlap + 1
    print(totalOverlap)                    

main()
