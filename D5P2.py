
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
        d = False
        h = False
        v = False
        slope = 0.0

        xStart = int(arrayS[i][0])
        xEnd = int(arrayE[i][0])
        yStart = int(arrayS[i][1])
        yEnd = int(arrayE[i][1])

        if (xEnd-xStart) != 0:
            
            #print ('y end',yEnd)
            #print ('y Start',yStart)

            #print ('x end',xEnd)
            #print ('x Start',xStart)
            slope = float((yEnd-yStart)/(xEnd-xStart))

        #d
        if slope == 1 or slope == -1: 
            d = True

        #h
        elif arrayS[i][1] == arrayE[i][1]: 
            h = True

        #v
        elif arrayS[i][0] == arrayE[i][0]:
            v = True
            

        
        if d == True:
            count = 0
            if slope < 0:
                #print('- slope diagonal points start',xStart,yStart,'end',xEnd,yEnd)
                
                if xStart < xEnd:
                    for k in range(xStart, xEnd+1):
                            #print((xStart+count),(yStart-count))
                            overlapGrid[yStart-count][xStart+count] = overlapGrid[yStart-count][xStart+count] + 1
                            count = count + 1
                else:
                    for k in range(xEnd, xStart+1):
                            overlapGrid[yEnd-count][xEnd+count] = overlapGrid[yEnd-count][xEnd+count] + 1
                            count = count + 1
                #print(overlapGrid)
            elif slope>0:
                #print('- slope diagonal points start',xStart,yStart,'end',xEnd,yEnd)
                if xStart < xEnd:
                    for k in range(xStart, xEnd+1):
                        #print('entered less than for lat check')  
                        #print((xStart+count),(yStart+count))
                        overlapGrid[yStart+count][xStart+count] = overlapGrid[yStart+count][xStart+count] + 1
                        count = count + 1
                else:
                    for k in range(xEnd, xStart+1):
                        overlapGrid[yStart-count][xStart-count] = overlapGrid[yStart-count][xStart-count] + 1
                        count = count + 1
                #print(overlapGrid)
        
        elif h == True:
            if xStart < xEnd:
                for k in range(xStart, xEnd+1):
                    overlapGrid[yStart][k] = overlapGrid[yStart][k] + 1
            else:
                for k in range(xEnd, xStart+1):
                    overlapGrid[yStart][k] = overlapGrid[yStart][k] + 1

        elif v == True:
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
    print(overlapGrid)
    print(totalOverlap)                    

main()
