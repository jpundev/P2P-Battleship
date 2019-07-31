import numpy as np


class BattleShip:
    def __init__(self, initINFO):
        '''
        :param initINFO:
        initINFO is a dictionary formatted as
        {'carrier':[pos,ori],
         'battleship':[pos,ori],
         'cruiser':[pos,ori],
         'submarine':[pos,ori],
         'destroyer':[pos,ori]}

         pos is a tuple (x,y)
         ori is a int like 0, 1, 2, 3
        '''

        #variable contains all possible hit location, used for checking placement overlap
        self.globalHitMap = []

        #indicate if it's your turn or not
        self.turn = None

        #Opponent's board
        self.OPPboard = None

        # import the position of each ship from initINFO (type dict)
        # self.ships, index0=carrier, index1=battleship, index2=cruiser, index3=submarine, index4=destoryer
        self.ships = []
        self.ships.append(
            {'pos': initINFO['carrier'][0], 'ori': initINFO['carrier'][1], 'health': 5, 'sunk': False, 'hitmap': []})
        self.ships.append(
            {'pos': initINFO['battleship'][0], 'ori': initINFO['battleship'][1], 'health': 4, 'sunk': False,
             'hitmap': []})
        self.ships.append(
            {'pos': initINFO['cruiser'][0], 'ori': initINFO['cruiser'][1], 'health': 3, 'sunk': False, 'hitmap': []})
        self.ships.append({'pos': initINFO['submarine'][0], 'ori': initINFO['submarine'][1], 'health': 3, 'sunk': False,
                           'hitmap': []})
        self.ships.append({'pos': initINFO['destroyer'][0], 'ori': initINFO['destroyer'][1], 'health': 2, 'sunk': False,
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
                for j in range(i['health']):
                    pos_temp[1] += 1
                    i['hitmap'].append(tuple(pos_temp))
                    if not self.placementOverlap(tuple(pos_temp)) and self.indexInRange(tuple(pos_temp)):
                        self.globalHitMap.append(tuple(pos_temp))
                    else:
                        print("error in ship placement, make sure the ship don't overlap or go outside of the board")
                        exit(1)

            elif i['ori'] == 1:
                for j in range(i['health']):
                    pos_temp[0] += 1
                    i['hitmap'].append(tuple(pos_temp))
                    if not self.placementOverlap(tuple(pos_temp)) and self.indexInRange(tuple(pos_temp)):
                        self.globalHitMap.append(tuple(pos_temp))
                    else:
                        print("error in ship placement, make sure the ship don't overlap or go outside of the board")
                        exit(1)

            elif i['ori'] == 2:
                for j in range(i['health']):
                    pos_temp[1] -= 1
                    i['hitmap'].append(tuple(pos_temp))
                    if not self.placementOverlap(tuple(pos_temp)) and self.indexInRange(tuple(pos_temp)):
                        self.globalHitMap.append(tuple(pos_temp))
                    else:
                        print("error in ship placement, make sure the ship don't overlap or go outside of the board")
                        exit(1)

            elif i['ori'] == 3:
                for j in range(i['health']):
                    pos_temp[0] -= 1
                    i['hitmap'].append(tuple(pos_temp))
                    if not self.placementOverlap(tuple(pos_temp)) and self.indexInRange(tuple(pos_temp)):
                        self.globalHitMap.append(tuple(pos_temp))
                    else:
                        print("error in ship placement, make sure the ship don't overlap or go outside of the board")
                        exit(1)

            else:
                print("invalid orientation input")
                exit(1)

    #return true if ship is placed outside of the board
    def indexInRange(self, pos):
        if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
            return True
        return False

    #return true if 2 ships overlaps
    def placementOverlap(self, pos):
        if pos in self.globalHitMap:
            return True
        return False

    # create a 2D numpy array, fill with '?'
    def createBoard(self):
        temp = []
        for i in range(64):
            temp.append('?')
        self.OPPboard = np.reshape(np.array(temp), (-1, 8))

    # update the board according to status and pos
    # pos is a tuple (x, y) and status may equal to 0(miss), 1(hit)
    def updateBoard(self, pos, status):
        if status == 0:
            self.OPPboard[pos[0]][pos[1]] = 'O'
        else:
            self.OPPboard[pos[0]][pos[1]] = 'X'
        print("kerry sucks")
        self.printBoard()

    # return 0 if no hit, return 1 for hit, return 2 for hit and sunk
    def checkAttack(self, pos):
        for i in self.ships:
            if pos in i['hitmap']:
                i['hitmap'].remove(pos)
                i['health'] -= 1
                if i['health'] == 0:
                    return 2  # hit and sunk ship
                return 1  # hit ship
        return 0  # no hit

    # if all ship is sunk, return True
    def defeated(self):
        defeated = True
        for i in self.ships:
            if i['sunk'] is False:
                defeated = False
                return defeated
        return defeated

    #print out board with format
    def printBoard(self):
        for i in range(8):
            line = "|"
            for j in range(8):
                line += self.OPPboard[i][j]
                line += "|"
            print(line)