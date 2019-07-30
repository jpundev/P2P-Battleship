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

        #import the position of each ship from initINFO (type dict)
        #self.ships, index0=carrier, index1=battleship, index2=cruiser, index3=submarine, index4=destoryer
        self.ships = []
        self.ships.append({'pos':initINFO['carrier'][0], 'ori':initINFO['carrier'][1], 'health':5, 'sunk':False, 'hitmap':[]})
        self.ships.append({'pos':initINFO['battleship'][0], 'ori':initINFO['battleship'][1], 'health':4, 'sunk':False, 'hitmap':[]})
        self.ships.append({'pos':initINFO['cruiser'][0], 'ori':initINFO['cruiser'][1], 'health':3, 'sunk':False, 'hitmap':[]})
        self.ships.append({'pos':initINFO['submarine'][0], 'ori':initINFO['submarine'][1], 'health':3, 'sunk':False, 'hitmap':[]})
        self.ships.append({'pos':initINFO['destroyer'][0], 'ori':initINFO['destroyer'][1], 'health':2, 'sunk':False, 'hitmap':[]})

        #create empty board
        self.createBoard()
        #check if ship placement is valid
        self.checkPlacement()
        #create hit position
        self.createHitMap()

    #create hit position
    def createHitMap(self):
        for i in self.ships:
            i['hitmap'].append(i['pos'])
            pos_temp = list(i['pos'])
            if i['ori'] == 0:
                for j in range(i['health']):
                    pos_temp[0] += 1
                    i['hitmap'].append(tuple(pos_temp))
            elif i['ori'] == 1:
                for j in range(i['health']):
                    pos_temp[1] -= 1
                    i['hitmap'].append(tuple(pos_temp))
            elif i['ori'] == 2:
                for j in range(i['health']):
                    pos_temp[0] -= 1
                    i['hitmap'].append(tuple(pos_temp))
            elif i['ori'] == 3:
                for j in range(i['health']):
                    pos_temp[1] += 1
                    i['hitmap'].append(tuple(pos_temp))
            else:
                print("invalid orientation input")
                exit(1)

    def checkPlacement(self):
        pass

    #create a 2D numpy array, fill with '?'
    def createBoard(self):
        temp = []
        for i in range(64):
            temp.append('?')
        self.OPPboard = np.reshape(np.array(temp), (-1, 8))

    #update the board according to status and pos
    #pos is a tuple (x, y) and status may equal to 0(miss), 1(hit)
    def updateBoard(self, pos, status):
        if status == 0:
            self.OPPboard[pos[0]][pos[1]] = 'O'
        else:
            self.OPPboard[pos[0]][pos[1]] = 'X'

    #return 0 if no hit, return 1 for hit, return 2 for hit and sunk
    def checkAttack(self, pos):
        for i in self.ships:
            if pos in i['hitmap']:
                i['hitmap'].remove(pos)
                i['health'] -= 1
                if i['health'] == 0:
                    return 2 #hit and sunk ship
                return 1 #hit ship
        return 0 #no hit

