import numpy as np
from os import system as sys


class BattleShip:
    def __init__(self, initINFO):
        """
        initINFO is a dictionary formatted as:
        {
            'carrier':[pos,ori],
            'battleship':[pos,ori],
            'cruiser':[pos,ori],
            'submarine':[pos,ori],
            'destroyer':[pos,ori]
         }

         pos is a tuple (row num,column num), it signifies as the bow of the ship
         ori is a int like 0, 1, 2, 3
            0 means the stern of the ship is to east of the bow
            1 means the stern of the ship is to south of the bow
            2 means the stern of the ship is to west of the bow
            3 means the stern of the ship is to north of the bow
        """

        # variable contains all possible hit location, used for checking placement overlap
        self.globalHitMap = []

        # indicate if it's your turn or not
        self.turn = None

        # Opponent's board
        self.guessBoard = None

        # import the position of each ship from initINFO (type dict)
        # self.ships, index0=carrier, index1=battleship, index2=cruiser, index3=submarine, index4=destroyer
        self.ships = []
        self.ships.append({'pos': initINFO['carrier'][0],
                           'ori': initINFO['carrier'][1],
                           'health': 5,
                           'sunk': False,
                           'hitmap': []})
        self.ships.append({'pos': initINFO['battleship'][0],
                           'ori': initINFO['battleship'][1],
                           'health': 4,
                           'sunk': False,
                           'hitmap': []})
        self.ships.append({'pos': initINFO['cruiser'][0],
                           'ori': initINFO['cruiser'][1],
                           'health': 3,
                           'sunk': False,
                           'hitmap': []})
        self.ships.append({'pos': initINFO['submarine'][0],
                           'ori': initINFO['submarine'][1],
                           'health': 3,
                           'sunk': False,
                           'hitmap': []})
        self.ships.append({'pos': initINFO['destroyer'][0],
                           'ori': initINFO['destroyer'][1],
                           'health': 2,
                           'sunk': False,
                           'hitmap': []})

        # create empty board
        self.createBoard()
        # create hit position
        self.createHitMap()

    # create hit position
    def createHitMap(self):
        for i in self.ships:
            i['hitmap'].append(i['pos'])
            pos_temp = list(i['pos'])
            if i['ori'] == 0:
                for j in range(i['health'] - 1):
                    pos_temp[1] += 1
                    self.placementCheck(pos_temp, i)
            elif i['ori'] == 1:
                for j in range(i['health'] - 1):
                    pos_temp[0] += 1
                    self.placementCheck(pos_temp, i)
            elif i['ori'] == 2:
                for j in range(i['health'] - 1):
                    pos_temp[1] -= 1
                    self.placementCheck(pos_temp, i)
            elif i['ori'] == 3:
                for j in range(i['health'] - 1):
                    pos_temp[0] -= 1
                    self.placementCheck(pos_temp, i)
            else:
                print("invalid orientation input")
                exit(1)

    # called in createHitMap(), it uses indexInRange() and placementOverlap to check the validity of the placement
    def placementCheck(self, pos_temp, i):
        i['hitmap'].append(tuple(pos_temp))
        # if the placement is valid, add that to the self.globalHitMap and continue
        # if not valid, print error and exit
        if not self.placementOverlap(tuple(pos_temp)) and self.indexInRange(tuple(pos_temp)):
            self.globalHitMap.append(tuple(pos_temp))
        else:
            print("error in ship placement, make sure the ships don't overlap or go outside of the board")
            exit(1)

    # return true if ship is placed outside of the board
    def indexInRange(self, pos):
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
            return True
        return False

    # return true if 2 ships overlaps
    def placementOverlap(self, pos):
        if pos in self.globalHitMap:
            return True
        return False

    # create a 2D numpy array, fill with '?'
    def createBoard(self):
        temp = []
        for i in range(64):
            temp.append('?')
        self.guessBoard = np.reshape(np.array(temp), (-1, 8))

    # update the board according to status and pos
    # clear window, print message according to status, print board
    # pos is a tuple (row num, col num) and status may equal to 0(miss), 1(hit)
    # 'X' means a hit 'O' means a miss
    def updateBoard(self, pos, status):
        sys("Clear")
        if status == 0:
            self.guessBoard[pos[0]][pos[1]] = 'O'
            print("Oops, you missed!")
        else:
            if self.guessBoard[pos[0]][pos[1]] == '?':
                self.guessBoard[pos[0]][pos[1]] = 'X'
                if status == 1:
                    print("Hooray!!! You hit something")
                else:
                    print("You just sunk a ship! Flex tape can't fix that!")
        self.printGuessBoard()

    # return 0 if no hit, return 1 for hit, return 2 for hit and sunk
    def checkAttack(self, pos):
        for i in self.ships:
            if pos in i['hitmap']:
                i['hitmap'].remove(pos)
                i['health'] -= 1
                if i['health'] == 0:
                    print("Oh no! The enemy has sunk one of your ship!")
                    return 2  # hit and sunk ship
                print("Damn it! We've been hit!")
                return 1  # hit ship
        print("The enemy missed! We Won't make the same mistake.")
        return 0  # no hit

    # if all ship is sunk, return True
    def defeated(self):
        for i in self.ships:
            if i['sunk'] is False:
                return False
        return True

    # print out board with format
    def printGuessBoard(self):
        print("   0 1 2 3 4 5 6 7 ")
        rowIndex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(8):
            line = rowIndex[i] + " |"
            for j in range(8):
                line += self.guessBoard[i][j]
                line += "|"
            print(line)



