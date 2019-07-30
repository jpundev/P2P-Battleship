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



    
        

    
    
    




    return




















if __name__ == '__main__':
    main()
    pass
