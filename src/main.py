import random
from os import system as sys
import platform
import numpy as np
from class_COM import COM
from class_battleship import BattleShip
from class_setup import Setup


def main():
    # Gether Inputs for Socket usage and connection
    sys("clear")
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
        except KeyboardInterrupt:
            print("Interrupted")
            exit(1)

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
    sockets.stop()
    return


# Function to send an attack
def attacksocket(board, sockets):
    # get user coord attack in form (x y) and set turn to false to indicate not my turn
    while True:
        attack = input("Your Turn! Make an attack! eg. A1 \n")
        tp = TranslateCoordinate(list(attack))
        x, y = tp[0], tp[1]
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
    # calls upon class_setup to get user input and generates a dictionary for class_battleship
    setup = Setup()
    return setup.main()


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


def TranslateCoordinate(string):
    rowIndex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    rowLetter = string[0]
    rowNum = rowIndex[rowLetter]
    return tuple([rowNum, int(string[1])])


if __name__ == '__main__':
    if platform.system() == 'Windows':
        print("Oops, looks like you are using WINDOWS. This program only runs on MacOs and Linux")
        exit(1)
    else:
        main()
