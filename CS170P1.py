import sys
import time

goalPuzzle = (['1', '2', '3', ], ['4', '5', '6'], ['7', '8', '0'])

def main():
    print('Welcome to the 8 Puzzle Solver \n')
    UserPuzzle = userChoice()
    strat = userStrategy()

def userChoice():
    print('Would you like to use our puzzle or create youf own?\n')
    userInput = input('Press 1 to see ours, or 2 if you want to create your own')
    uInput = int(userInput)
    if uInput == 1:
       puzzle = (['1', '3', '5', ], ['4', '6', '8'], ['2', '7', '8'])
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
    puzzle = row1, row2, row3
    return puzzle

def userStrategy():
    print('Which strategy would you like to use: \n')
    print('Uniform Cost Search\n')
    print('A* with the Misplaced Tile heuristic\n')
    print('A* with the manhattan distance\n')
    userStrategyC = input(' ')
    return userStrategyC

    
if __name__ == '__main__':
            main()