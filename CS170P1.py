import queue
import sys


def main():
    print('Welcome to the 8 Puzzle Solver \n')
    print('Would you like to use our puzzle, or create your own? \n')
    userInput = input('Press 1 for the default and 2 if you want to input your own!')
    choice = int(userInput)

    if choice == 1:
        puzzle = (['1', '3', '5', ], ['4', '6', '8'], ['2', '7', '8'])
    elif choice == 2:
        print('Please begin entering your puzzle and use 0 to represent a blank spot \n')
        
if __name__ == '__main__':
        main()
