from os import system as sys

import numpy as np


# getting all the placement for class_battleship
# handles and sanitize user input
class Setup:
    def __init__(self):
        # board to display
        self.myBoard = None

        # to be returned at the end as initINFO for class_battleship
        self.placement = {}

    def main(self):
        # finished getting input
        done = False

        while not done:
            # clear screen
            sys("clear")

            # create empty board
            self.createBoard()

            # get input
            for i in range(5):
                self.getInput(i)

            # print out final board and get confirmation, if confirmed, exit and return placement
            # reset board and placement if user do not confirm, restart the get user input process
            sys("clear")
            self.drawBoard()
            confirm = input("This is your board, do you with to continue? [Y/n]: ")
            if confirm.upper() == 'Y':
                done = True
            else:
                # reset placement
                self.placement = {}

        # return placement
        return self.placement

    def createBoard(self):
        temp = []
        for i in range(64):
            temp.append('?')
        self.myBoard = np.reshape(np.array(temp), (-1, 8))

    def drawBoard(self):
        print("   0 1 2 3 4 5 6 7 ")
        rowIndex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(8):
            line = rowIndex[i] + " |"
            for j in range(8):
                line += self.myBoard[i][j]
                line += "|"
            print(line)

    def updatedBoard(self, pos_t, ori, shipNum):
        shipHeath = [5, 4, 3, 3, 2]
        self.myBoard[pos_t[0]][pos_t[1]] = "\u25C9"
        pos_row = pos_t[0]
        pos_col = pos_t[1]

        for i in range(shipHeath[shipNum] - 1):
            if ori == 0:
                pos_col += 1
                self.myBoard[pos_row][pos_col] = "\u25C9"
            elif ori == 1:
                pos_row += 1
                self.myBoard[pos_row][pos_col] = "\u25C9"
            elif ori == 2:
                pos_col -= 1
                self.myBoard[pos_row][pos_col] = "\u25C9"
            elif ori == 3:
                pos_row -= 1
                self.myBoard[pos_row][pos_col] = "\u25C9"

    # ship num range from 0 - 4, 0 being the carrier, 4 being the destroyer
    def getInput(self, shipNum):
        gotValidInput = False

        prompt = ["Enter a coordinate and orientation for the carrier (5) eg. A1 3",
                  "Enter a coordinate and orientation for the battleship (4) eg. A1 3",
                  "Enter a coordinate and orientation for the submarine (3) eg. A1 3",
                  "Enter a coordinate and orientation for the cruiser (3) eg. A1 3",
                  "Enter a coordinate and orientation for the destroyer (2) eg. A1 3"]

        ships = ['carrier', 'battleship', 'submarine', 'cruiser', 'destroyer']

        while not gotValidInput:
            # clear screen
            sys("clear")

            # draw out the board
            self.drawBoard()

            # get and process input
            print(prompt[shipNum])
            placement = input().split()
            pos = placement[0]
            ori = int(placement[1])

            # validating input
            if len(pos) == 2:  # validating pos
                rowIndex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                if pos[0] in rowIndex and 0 <= int(pos[1]) <= 7:
                    if 0 <= ori <= 3:  # validating ori
                        gotValidInput = True

            # break if input is not valid
            if not gotValidInput:
                print("Invalid Input, Please try again!")
                break
            else:  # updated self.placement and self.gussBoard if inputs are valid
                pos_t = self.translateCoordinate(pos)  # position as a int a tuple
                self.placement[ships[shipNum]] = [pos_t, ori]
                self.updatedBoard(pos_t, ori, shipNum)

    @staticmethod
    def translateCoordinate(string):
        rowIndex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        rowLetter = string[0]
        rowNum = rowIndex[rowLetter]
        return tuple([rowNum, int(string[1])])
