from class_battleship import BattleShip
from class_COM import COM
import random 

def main():
    #Gether Inputs for Socket usage and connection
    input("Welcome To Our BattleShip Game, Press Any Button to Continue...\n")
    OPPip = input("Enter Your opponents IP..\n")
    txport = input("Enter Transmitting port..\n")
    rxport = input("Enter Receiving Port...\n")
    host = input("Are you the Host? (y/n) \n")
    sockets = COM(OPPip,txport,rxport)


    
    board = initBoard()
    
    

    #Is Host
    if(host == "y"):
        print("Waiting for Player 2 to Connect..\n")
        connectedmsg = sockets.recieve()
        print("Player 2 is.." + connectedmsg)
        #Going First
        if(random.randint(1,2)==1):
            sockets.connect()
            sockets.send("f")
        #Going Second
        else:
            sockets.connect()
            sockets.send("s")


    #is not host
    else:
        print("Connecting to Host..\n")
        sockets.connect()
        sockets.send("Connected")
        connectedmsg = sockets.recieve()
        #Going Second
        if(connectedmsg == "f"):
            

        #Going First
        elif (connectedmsg == "s"):

def initBoard():

    dictionary = {"battleship":None,"carrier":None,"submarine":None,"cruiser":None,"destroyer":None}
    print("Orientation is [ 0 : right, 1: down, 2: left, 3: right\n Coordinates must be entered from 0-7 like this (1,2)\n")
    dictionary["carrier"] = parser(input("Enter a coordinate and orientation for the carrier (5) eg. 1 2 3 \n"))
    dictionary["battleship"] = parser(input("Enter a coordinate and orientation for the battleship (4) eg. 1 2 3 \n"))
    dictionary["submarine"] = parser(input("Enter a coordinate and orientation for the submarine (3) eg. 1 2 3 \n"))
    dictionary["cruiser"] = parser(input("Enter a coordinate and orientation for the cruiser (3) eg. 1 2 3 \n"))
    dictionary["destroyer"] = parser(input("Enter a coordinate and orientation for the destroyer (2) eg. 1 2 3 \n"))
    


    

    
        
def parser(string):
    stringarray = string.split(" ")
    coordarray = [int(stringarray[0]),int(stringarray[1])]
    return [tuple(coordarray),int(stringarray[1])]

    
    
    




    




















if __name__ == '__main__':
    main()
    pass
