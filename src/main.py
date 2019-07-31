from class_battleship import BattleShip
from class_COM import COM
import random


def main():
    # Gether Inputs for Socket usage and connection
    input("Welcome To Our BattleShip Game, Press Any Button to Continue...\n")
    OPPip = input("Enter Your opponents IP..\n")
    txport = input("Enter Transmitting port..\n")
    rxport = input("Enter Receiving Port...\n")
    host = input("Are you the Host? (y/n) \n")
    # Initialize Sockets and board
    sockets = COM(OPPip, txport, rxport)
    while True:
        try:
            boarddict = initBoard()
            board = BattleShip(boarddict)
            break
        except:
            pass
    # Identify if the player is host from the userinput
    if (host == "y"):
        print("Waiting for Player 2 to Connect..\n")
        # Socket listen and block for player 2 send the connected message
        sockets.listen()
        connectedmsg = sockets.recieve()
        print("Player 2 is.." + connectedmsg)
        # Player1 is going first
        if (random.randint(1, 2) == 1):
            # Connect socket and initialize first strike
            sockets.connect()
            attacksocket(board, sockets)
            board.turn = False
            game(board, sockets)

        # Going Second
        else:
            # Connect socket and inform player2 that player1 will be going second.
            sockets.connect()
            sockets.send("s")
            # Check if the attack hit and update the board
            recieveAttack(board, sockets)
            board.turn = True
            game(board, sockets)


    # Player1 is not the host AKA player2.
    else:
        print("Connecting to Host..\n")
        # Connect socket and send that this player is connected
        sockets.connect()
        sockets.send("Connected")
        # Listen message to identify who is going first
        sockets.listen()
        connectedmsg = sockets.recieve()
        # Going Second
        if (connectedmsg != "s"):
            # Check if the attack hit and update the board
            value = board.checkAttack(connectedmsg)
            sendvalue(value, sockets)
            board.turn = True
            game(board, sockets)

        # Going First
        elif (connectedmsg == "s"):
            attacksocket(board, sockets)
            game(board, sockets)


def game(board, sockets):
    # While loop until game ends where player has all of ships sunk
    while not board.defeated():
        # If players turn
        if (board.turn):
            attacksocket(board, sockets)
        # Not players turn
        else:
            recieveAttack(board, sockets)
    return


# Function to send an attack
def attacksocket(board, sockets):
    # get user coord attack in form (x y) and set turn to false to indicate not my turn
    while True:
        attack = input("Your Turn! Make an attack! eg. A1 \n")
        tp = TranslateCoordinate(list(attack))
        x,y = tp[0],tp[1]
        if (0 <= x <= 7 or 0 <= y <= 7):
            break
        else:
            print("Please Enter a Valid Coordinate")

        
    
    sockets.send(tp)
    board.turn = False
    recievemsg = sockets.recieve()
    if recievemsg == "Hit!":
       
        board.updateBoard(tp, 1)
    if recievemsg == "Hit and Sunk!":
        
        board.updateBoard(tp, 2)
    if recievemsg == "Miss!":
        
        board.updateBoard(tp, 0)


# Check if the attack hit and update the board
def recieveAttack(board, sockets):
    connectedmsg = sockets.recieve()
    value = board.checkAttack(connectedmsg)
    sendvalue(value, sockets)
    board.turn = True


# initialize the board to send to the board class
def initBoard():
    # Initialize the dictionary with empty positions
    dictionary = {"battleship": None, "carrier": None, "submarine": None, "cruiser": None, "destroyer": None}
    print(
        "Orientation is [ 0 : right, 1: down, 2: left, 3: right\n Coordinates must be entered beginning with a letter and then a number \n")
    # Get every battle ship orientation and position and put them into the dictionary
    
    dictionary["carrier"] = parser(input("Enter a coordinate and orientation for the carrier (5) eg. A1 3 \n"))
    dictionary["battleship"] = parser(input("Enter a coordinate and orientation for the battleship (4) eg. A1 3 \n"))
    dictionary["submarine"] = parser(input("Enter a coordinate and orientation for the submarine (3) eg. A1 3 \n"))
    dictionary["cruiser"] = parser(input("Enter a coordinate and orientation for the cruiser (3) eg. A1 3 \n"))
    dictionary["destroyer"] = parser(input("Enter a coordinate and orientation for the destroyer (2) eg. A1 3 \n"))

    return dictionary


# Function that prints out status of the missile that you sent
def hit(value):
    if value == 0:
        return "Miss!\n"
    if value == 1:
        return "Hit!\n"
    if value == 2:
        return "Hit and Sunk!\n"


def sendvalue(value, sockets):
    if value == 0:
        sockets.send("Miss!")
    if value == 1:
        sockets.send("Hit!")
    if value == 2:
        sockets.send("Hit and Sunk!")


# helper function to parse the user input for the correct output for our battleship class
def parser(string):
    stringarray = string.split(" ")
    print(stringarray)
    tp = TranslateCoordinate(stringarray[0])
    x,y = tp[0],tp[1]
    while True:
        if (0 <= x <= 7 or 0 <= y <= 7):       
            return [tp, int(stringarray[1])]
        else:
            print("Please Enter a Valid Coordinate")

def TranslateCoordinate(string):
    rowIndex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    rowLetter = string[0]
    rowNum = rowIndex[rowLetter]
    return tuple([rowNum, int(string[1])])

if __name__ == '__main__':
    main()
    pass
