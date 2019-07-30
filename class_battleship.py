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
        self.ships = {}
        self.ships['carrier'] = {'pos':initINFO['carrier'][0], 'ori':initINFO['carrier'][1], 'health':5, 'sunk':False}
        self.ships['battleship'] = {'pos':initINFO['battleship'][0], 'ori':initINFO['battleship'][1], 'health':4, 'sunk':False}
        self.ships['cruiser'] = {'pos':initINFO['cruiser'][0], 'ori':initINFO['cruiser'][1], 'health':3, 'sunk':False}
        self.ships['submarine'] = {'pos':initINFO['submarine'][0], 'ori':initINFO['submarine'][1], 'health':3, 'sunk':False}
        self.ships['destroyer'] = {'pos':initINFO['destroyer'][0], 'ori':initINFO['destroyer'][1], 'health':2, 'sunk':False}

        #create empty board
        self.createBoard()

    def createHitMap(self):
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

