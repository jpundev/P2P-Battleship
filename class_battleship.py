import class_COM
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
        self.createHitMap()

    #
    def createHitMap(self):
        for i in self.ships:
            i['hitmap'].append(i['pos'])
            pos_temp = [i['pos'][0], i['pos'][1]]
            if i['ori'] == 0:
                for j in range(i['health']):
                    pos_temp[0] += 1
                    i['hitmap'].append(i['pos'])
            elif i['ori'] == 1:
                pass
            elif i['ori'] == 2:
                pass
            elif i['ori'] == 3:
                pass

    def checkPlacement(self):
        pass

    def createBoard(self):
        temp = []
        for i in range(64):
            temp.append('?')
        self.OPPboard = np.reshape(np.array(temp), (-1, 8))

    def attack(self, pos):
        pass

    def checkAttack(self, pos):
        pass

