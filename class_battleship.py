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
        self.carrier = {'pos':initINFO['carrier'][0], 'ori':initINFO['carrier'][1], 'health':5, 'sunk':False}
        self.battleship = {'pos':initINFO['battleship'][0], 'ori':initINFO['battleship'][1], 'health':4, 'sunk':False}
        self.cruiser = {'pos':initINFO['cruiser'][0], 'ori':initINFO['cruiser'][1], 'health':3, 'sunk':False}
        self.submarine = {'pos':initINFO['submarine'][0], 'ori':initINFO['submarine'][1], 'health':3, 'sunk':False}
        self.destroyer = {'pos':initINFO['destroyer'][0], 'ori':initINFO['destroyer'][1], 'health':2, 'sunk':False}

        self.OPPboard = None
        self.createBoard()
        print(self.OPPboard)

    def checkPlacement(self):
        pass

    def createBoard(self):
        temp = []
        for i in range(64):
            temp.append('?')
        self.OPPboard = np.reshape(np.array(temp), (-1, 8))

    def attack(self,):