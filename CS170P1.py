import sys
import copy

goalPuzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


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
        puzzle = [[1, 2, 3, ], [7, 8, 0], [4, 5, 6]]
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
    row2 = input('Please enter your second row:\n')
    row2 = row2.split(' ')
    row3 = input('Please enter your third row :\n')
    row3 = row3.split(' ')
    for i in range(0, 3):
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
    x = int(userStrategyC)
    return x


def misplaced(puzzle):
    sum = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0 and puzzle[i][j] != goalPuzzle[i][j]:
                sum += 1
    return sum


def manhattanD(PuzzlePassedin):
    fCount = 0
    rows = 0
    columns = 0
    gRows = 0
    gColumns = 0

    for i in range(1, 9):
        for j in range(3):
            for k in range(3):
                if int(PuzzlePassedin[j][k]) == i:
                    rows = j
                    columns = k
                if goalPuzzle[j][k] == i:
                    gRows = j
                    gColumns = k
        fCount += abs(gRows - rows) + abs(gColumns - columns)

    return fCount


class node:
    def __init__(self, puzzle ):
        self.puzzle = puzzle
        # puzzle is just our puzzle
        self.depth = 0
        self.cost = 0
        self.depth = 0


def node_expansion(NodePassed, totalExpansion):
    seen = [] #this is a list of seen puzzles so we dont have to worry about repeated states
    depth = NodePassed.depth + 1
    neRow = 0
    neColumns = 0
    for i in range(3):
        for j in range(3):
            if NodePassed.puzzle[i][j] == 0:
                neRow = i 
                neColumns = j

    if neRow > 0:
        top = copy.deepcopy(NodePassed.puzzle)
        top[neRow][neColumns] = top[neRow - 1][neColumns]
        top[neRow - 1][neColumns] = 0
        topNode = node(top)
        topNode.depth = depth
        seen.append(topNode)
        totalExpansion += 1

    if neColumns >  0:
        left = copy.deepcopy(NodePassed.puzzle)
        left[neRow][neColumns] = left[neRow][neColumns - 1]
        left[neRow][neColumns - 1] = 0
        leftNode = node(left)
        leftNode.depth = depth
        seen.append(leftNode)
        totalExpansion += 1
    

    if neRow < 2:
        bottom = copy.deepcopy(NodePassed.puzzle)
        bottom[neRow][neColumns] = bottom[neRow + 1][neColumns]
        bottom[neRow + 1][neColumns] = 0
        bottomNode = node(bottom)
        bottomNode.depth = depth
        seen.append(bottomNode)
        totalExpansion += 1

    elif neColumns < 2:
        right = copy.deepcopy(NodePassed.puzzle)
        right[neRow][neColumns] = right[neRow][neColumns + 1]
        right[neRow][neColumns + 1] = 0
        rightNode = node(right)
        rightNode.depth = depth
        seen.append(rightNode)
        totalExpansion += 1
        
    return  seen, totalExpansion



def searchAlg(OGPuzzle, choiceUser):
    TotalExploredNodes = 0
    max_queue = 0
    queueList = []
    GoalState = False
    if choiceUser == 1:
        firstNode = node(OGPuzzle)
        h = 0
        firstNode.cost = h
        firstNode.depth = 0

    if choiceUser == 2:
        h = misplaced(OGPuzzle)
        firstNode = node(OGPuzzle)
        firstNode.cost = h
        firstNode.depth = 0

    if choiceUser == 3:
        h = manhattanD(OGPuzzle)
        firstNode = node(OGPuzzle)
        firstNode.cost = h
        firstNode.depth = 0
    

    queueList.append(firstNode)
    while not GoalState:

        if len(queueList) == 0:
            print ("Queue is empty, please fill it")

        new_node = queueList.pop()

        if new_node.puzzle == goalPuzzle:
            GoalState = True
            print ('To solve this problem the search algorithm expanded a total of ', TotalExploredNodes - 3 , 'nodes.')
            print ('The maximum number of nodes in the queue at any one time was ' , max_queue - 1 , '.')
            print ('The depth of the goal node was ' , new_node.depth , '.')

        else:
            SeenList, TotalExploredNodes = node_expansion(new_node, TotalExploredNodes)
            for x in range(len(SeenList)):
                if choiceUser == 1:
                    SeenList[x].heuristic = 0
                if choiceUser == 2:
                    SeenList[x].heuristic = misplaced(SeenList[x].puzzle)
                    SeenList[x].cost = SeenList[x].heuristic + SeenList[x].depth
                if choiceUser == 3:
                    SeenList[x].heuristic = manhattanD(SeenList[x].puzzle)
                    SeenList[x].cost = SeenList[x].heuristic + SeenList[x].depth
                queueList.append(SeenList[x])
                if max_queue < len(queueList):
                    max_queue = len(queueList)
    print(new_node.puzzle[0][0],new_node.puzzle[0][1],new_node.puzzle[0][2])
    print(new_node.puzzle[1][0],new_node.puzzle[1][1],new_node.puzzle[1][2])
    print(new_node.puzzle[2][0],new_node.puzzle[2][1],new_node.puzzle[2][2], "\n")


if __name__ == '__main__':
    main()
