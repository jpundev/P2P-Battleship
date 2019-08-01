import numpy as np
from os import system as sys

# getting all the placement for class_battleship
# handles and sanitize user input
class Setup:
    def __init__(self):
        # board to display
        self.guessBoard = None

        # to be returned at the end as initINFO for class_battleship
        self.placement = {}

    def main(self):
        sys("clear")

        self.createBoard()

        for i in range(5):
            self.getInput(i)

        self.exit()


    def createBoard(self):
        temp = []
        for i in range(64):
            temp.append('?')
        self.guessBoard = np.reshape(np.array(temp), (-1, 8))

    def drawBoard(self):
        print("   0 1 2 3 4 5 6 7 ")
        rowIndex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(8):
            line = rowIndex[i] + " |"
            for j in range(8):
                line += self.guessBoard[i][j]
                line += "|"
            print(line)

    def updatedBoard(self, pos, ori):
        pass

    # ship num range from 0 - 4, 0 being the carrier, 4 being the destoryer
    def getInput(self, shipNum):
        gotValidInput = False

        prompt = ["Enter a coordinate and orientation for the carrier (5) eg. A1 3",
                  "Enter a coordinate and orientation for the battleship (4) eg. A1 3",
                  "Enter a coordinate and orientation for the submarine (3) eg. A1 3",
                  "Enter a coordinate and orientation for the cruiser (3) eg. A1 3",
                  "Enter a coordinate and orientation for the destroyer (2) eg. A1 3"]

        ships = ['carrier', 'battleship', 'submarine', 'cruiser', 'destroyer']

        while not gotValidInput:
            # draw out the board
            self.drawBoard()

            # get and process input
            print(prompt[shipNum])
            placement = input().split()
            pos = placement[0]
            ori = int(placement[1])

            # validating input
            if len(pos) == 2: # validating pos
                rowIndex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                if pos[0] in rowIndex and 0 <= int(pos[1]) <= 7:
                    if 0 <= ori <= 3:  # validating ori
                        gotValidInput = True

            # break if input is not valid
            if gotValidInput == False:
                print("Invalid Input, Please try again!")
                break;
            else: # updated self.placement and self.gussBoard if inputs are valid
                pos_t = self.TranslateCoordinate(pos)  # position as a int a tuple
                self.placement[ships[shipNum]] = [pos_t, ori]



    def TranslateCoordinate(self, string):
        rowIndex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        rowLetter = string[0]
        rowNum = rowIndex[rowLetter]
        return tuple([rowNum, int(string[1])])

    def exit(self):
        print(self.placement)
        return self.placement

a = Setup()
a.main()

