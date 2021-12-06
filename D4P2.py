
def checkHits(hitPos,set,avlBoards):
    row1 = [0,1,2,3,4]
    row2 = [5,6,7,8,9]
    row3 = [10,11,12,13,14]
    row4 = [15,16,17,18,19]
    row5 = [20,21,22,23,24]
    
    c1 = [0,5,10,15,20]
    c2 = [1,6,11,16,21]
    c3 = [2,7,12,17,22]
    c4 = [3,8,13,18,23]
    c5 = [4,9,14,19,24]
    
    #which board got hit
    boardHit = 0
    boardHit = int(hitPos/25)

    if boardHit not in avlBoards:
        print('rejecting check because board already won')
        return 0

    temp = hitPos
    while temp > 24:
        temp = temp -25
    
    row =1
    c = 1
    print('Board:',boardHit)
    if temp in row1:
        print('row 1 hit')
        for x in row1:
            if set[x+(boardHit*25)] != 1:
                row = 0
            
    if temp in row2:
        print('row 2 hit')
        for x in row2:
            if set[x+(boardHit*25)] != 1:
                row = 0
            
    if temp in row3:
        print('row 3 hit')
        for x in row3:
            if set[x+(boardHit*25)] != 1:
                row = 0
            
    if temp in row4:
        print('row 4 hit')
        for x in row4:
            if set[x+(boardHit*25)] != 1:
                row = 0
            
    if temp in row5:
        print('row 5 hit')
        for x in row5:
            if set[x+(boardHit*25)] != 1:
                row = 0
    if temp in c1:
        print('c 1 hit')
        for y in c1:
            if set[y+(boardHit*25)] != 1:
                c = 0
            
    if temp in c2:
        print('c 2 hit')
        for y in c2:
            if set[y+(boardHit*25)] != 1:
                c = 0
            
    if temp in c3:
        print('c 3 hit')
        for y in c3:
            if set[y+(boardHit*25)] != 1:
                c = 0
            
    if temp in c4:
        print('c 4 hit')
        for y in c4:
            if set[y+(boardHit*25)] != 1:
                c = 0
            
    if temp in c5:
        print('c 5 hit')
        for y in c5:
            if set[y+(boardHit*25)] != 1:
                c = 0
    
    if c == 0 and row == 0:
        return 0
    else:
        return boardHit
            

def main():
    
    winner = 0
    arrayBase = []
    arrayList = []
    arrayBoard = []
    arrayBoardHits = []
    arrayBoardHitsSnap = []
    remBoards= []

    #with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D3.txt","r") as f:
    #    firstline = f.readline().rstrip()
    #    binLen = len(str(firstline))

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D4.txt","r") as f:
        content = f.readlines()
        for val in content[0].split(','):
            arrayList.append(int(val))  

    with open(r"C:\Users\mpn42\source\repos\AdventOfCode2021\AdventOfCode2021\Input Files\D4_boards.txt","r") as f:
        for val in f.read().split():
            arrayBoard.append(int(val))

   
    #determines total number of boards
    numOfBoards= len(arrayBoard)/25

    #creates the array for detecting matches
    for i in range(0,len(arrayBoard)):
        arrayBoardHits.append(0)

    #creates list for available boards
    for x in range(0,int(numOfBoards)):
        remBoards.append(x)


    #starts calling numbers, determines winning board
    for val in arrayList:
        winner = 0
        #print(arrayBoardHits)
        for i in range(0,len(arrayBoard)):
            if arrayBoard[i] == val:
                total = 0
                for k in arrayBoardHitsSnap:
                    total = total + k

                print('sum of snapshot array',total)

                #print(arrayBoardHitsSnap)
                #marks the hit
                arrayBoardHits[i] = 1               
                #check if its a winner
                print('checking val hit', val)
                winner = checkHits(i,arrayBoardHits,remBoards)
                print('winner value right before chec',winner)
                if winner != 0:
                    print('removing',winner)
                    remBoards.remove(winner)
                    print('new remaining',remBoards)
                    winningNumber = val
                    lastWinner = winner
                    arrayBoardHitsSnap.clear()
                    for j in arrayBoardHits:
                        arrayBoardHitsSnap.append(j)

                else:
                    print('no winner')

    #determine start and end index of winning board
    print(winningNumber)
    print(lastWinner)
    start = lastWinner*25
    end = start +25
    sum = 0
    print(arrayBoardHitsSnap)
    for x in range(start,end):
        if arrayBoardHitsSnap[x] != 1:
            sum = sum + arrayBoard[x]
    print(sum)
    print(sum*winningNumber)


main()
