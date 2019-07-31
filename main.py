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
    #Initialize Sockets and board
    sockets = COM(OPPip,txport,rxport)
    boarddict = initBoard()
    board = BattleShip(boarddict)
    #Identify if the player is host from the userinput
    if(host == "y"):
        print("Waiting for Player 2 to Connect..\n")
        #Socket listen and block for player 2 send the connected message
        sockets.listen()
        connectedmsg = sockets.recieve()
        print("Player 2 is.." + connectedmsg)
        #Player1 is going first
        if(random.randint(1,2)==1):
            #Connect socket and initialize first strike 
            sockets.connect()
            attacksocket(board,sockets)
            game(board,sockets)

        #Going Second
        else:
            #Connect socket and inform player2 that player1 will be going second.
            sockets.connect()
            sockets.send("s")
            #Check if the attack hit and update the board
            recieveAttack(board,sockets)
            game(board,sockets)


    #Player1 is not the host AKA player2.
    else:
        print("Connecting to Host..\n")
        #Connect socket and send that this player is connected
        sockets.connect()
        sockets.send("Connected")
        #Listen message to identify who is going first
        sockets.listen()
        connectedmsg = sockets.recieve()
        #Going Second
        if(connectedmsg != "s"):
            #Check if the attack hit and update the board
            board.checkAttack(connectedmsg)
            board.turn = True
            game(board,sockets)

        #Going First
        elif (connectedmsg == "s"):
            attacksocket(board,sockets)
            game(board,sockets)

def game(board,sockets):
    #While loop until game ends where player has all of ships sunk
    while not board.defeated():
        #If players turn
        if (board.turn):
            attacksocket(board,sockets)
        #Not players turn
        else:
            recieveAttack(board,sockets)  
    return

#Function to send an attack
def attacksocket(board,sockets):
    #get user coord attack in form (x y) and set turn to false to indicate not my turn
    attack = input("Your Turn! Make an attack x y 0-7 \n")
    attackarray = attack.split(" ")
    print(tuple((int(attackarray[0]),int(attackarray[1]))))
    sockets.send(tuple((int(attackarray[0]),int(attackarray[1]))))
    board.turn = False

#Check if the attack hit and update the board
def recieveAttack(board,sockets):
    connectedmsg = sockets.recieve()
    board.checkAttack(connectedmsg)
    board.turn = True
    board.printBoard()
#initialize the board to send to the board class
def initBoard():

    #Initialize the dictionary with empty positions
    dictionary = {"battleship":None,"carrier":None,"submarine":None,"cruiser":None,"destroyer":None}
    print("Orientation is [ 0 : right, 1: down, 2: left, 3: right\n Coordinates must be entered from 0-7 like this (1,2)\n")
    #Get every battle ship orientation and position and put them into the dictionary
    dictionary["carrier"] = parser(input("Enter a coordinate and orientation for the carrier (5) eg. 1 2 3 \n"))
    dictionary["battleship"] = parser(input("Enter a coordinate and orientation for the battleship (4) eg. 1 2 3 \n"))
    dictionary["submarine"] = parser(input("Enter a coordinate and orientation for the submarine (3) eg. 1 2 3 \n"))
    dictionary["cruiser"] = parser(input("Enter a coordinate and orientation for the cruiser (3) eg. 1 2 3 \n"))
    dictionary["destroyer"] = parser(input("Enter a coordinate and orientation for the destroyer (2) eg. 1 2 3 \n"))
    

    return dictionary


    

    
#helper function to parse the user input for the correct output for our battleship class     
def parser(string):
    stringarray = string.split(" ")
    print(stringarray)
    coordarray = [int(stringarray[0]),int(stringarray[1])]
    print([tuple(coordarray),int(stringarray[2])])
    return [tuple(coordarray),int(stringarray[2])]

    
    
    




    




















if __name__ == '__main__':
    main()
    pass
