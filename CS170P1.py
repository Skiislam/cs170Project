import sys
import time
import copy

goalPuzzle = [[1, 2, 3, ], [4, 5, 6], [7, 8, 0]]

def main():
    print('Welcome to the 8 Puzzle Solver \n')
    puzzleUser = userChoice()
    strat = userStrategy()
    searchAlg(puzzleUser, strat)

    


def userChoice():
    print('Would you like to use our puzzle or create yourclear own?\n')
    userInput = input('Press 1 to use ours, or 2 if you want to create your own\n')
    uInput = int(userInput)
    if uInput == 1:
       puzzle = [[1, 3, 5,], [4, 6, 8], [2, 7, 8]]
       return puzzle
    elif uInput == 2:
        return userPuzzle()
    else:
        print("Error could not recongize input, please enter 1 or 2 only! \n")
        return userChoice()


def userPuzzle():
    print('Please Enter your puzzle with 0 to represent the blank spot \n')
    row1 = input('Please enter your first row seperating the numbers with a space:\n')
    row1 = row1.split(' ')
    row2= input('Please enter your second row:\n')
    row2 = row2.split(' ')
    row3 = input('Please enter your third row :\n')
    row3 = row3.split(' ')
    for i in range(0,3):
        row1[i] = int(row1[i])
        row2[i] = int(row2[i])
        row3[i] = int(row3[i])
    puzzle = [row1, row2, row3]
    return puzzle

def userStrategy():
    print('Which strategy would you like to use: \n')
    print('(1)Uniform Cost Search')
    print('(2)A* with the Misplaced Tile heuristic\n')
    print('(3)A* with the manhattan distance\n')
    userStrategyC = input('')
    return userStrategyC

def misplaced(puzzle):
    sum = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0 and puzzle[i][j] != goalPuzzle[i][j]:
                sum += 1
    print("This is the total for misplaced: ",sum, "\n")
    return sum

def manhattanD(PuzzlePassedin):
    
    fCount = 0
    rows = 0
    columns = 0
    gRows = 0
    gColumns = 0

    for i in range(1,9):
        for j in range(3):
            for k in range(3):
                if int(PuzzlePassedin[j][k]) == i:
                        rows = j
                        columns = k
                if goalPuzzle[j][k] == i:
                        gRows = j
                        gColumns = k
        fCount+= abs(gRows - rows) + abs(gColumns - columns)
        print("The Fcount is", fCount)
    return fCount

class node:
    def __init__(self, heuristic, puzzle, depth):
        self.puzzle = puzzle
        #puzzle is just our puzzle
        self.depth = depth
        self.heursitic = heuristic
        self.cost = depth + heuristic 
        #depth is the cost of how many nodes have been explored from start to current
        #Heuristic is the estimate on how much itll cost to get to the goal cost
        #Together the lowest cost value will be picked and that is how the algo will figure out how to get to goal state fastest and cheapest


def expandedNode(curr, totalExpansion):
    depth = curr.depth + 1
    seen = []
    rows = 0
    columns = 0
    for i in range(3):
        for j in range(3):
            if [i][j] == 0:
                row = i
                columns = j #We want to see where the 0 aka the blank space is so we look for it
                            #and set our rows and columns acoordingly 
    if columns > 0:
        left = copy.deepcopy(curr.puzzle)
        left[row][columns] = left[row][columns - 1]
        left[row][columns - 1] = 0
        leftNode = node(0, left, depth)
        seen.append(leftNode)
        totalExpansion+=1
    if rows > 0:
        top = copy.deepcopy(curr.puzzle)
        top[row][columns] = left[row][columns - 1]
        top[row][columns - 1] = 0
        topNode = node(0, top, depth) 
        seen.append(topNode)
        totalExpansion+=1
    if columns > 2:
        right = copy.deepcopy(curr.puzzle)
        right[row][columns] = right[row][columns - 1]
        right[row][columns - 1] = 0
        rightNode = node(0,right, depth)
        seen.append(rightNode)
        totalExpansion+=1
    if rows > 2:
        bottom = copy.deepcopy(curr.puzzle)
        bottom[row][columns] = bottom[row][columns - 1]
        bottom[row][columns - 1] = 0
        bottomNode = node(0,bottom, depth)
        seen.append(bottomNode)
        totalExpansion +=1
    return seen, totalExpansion

def searchAlg(userPuzzle, userChoice):
    max_queue = 0
    expansion = 0
    h = 0
    
    if userChoice == 1:
        initialState = node(0, userPuzzle, 0)
    if userChoice == 2:
        h = misplaced(userPuzzle)
        initialState = node(h, userPuzzle, 0)
    if userChoice == 3:
        h = manhattanD(userPuzzle)
        initialState = node(h,userPuzzle, 0)
    q = []
    
    
    
    
if __name__ == '__main__':
            main()