# P2P-Battleship 
![alt text](https://raw.githubusercontent.com/punjordi/P2P-Battleship/master/asset/banner.jpg)
##### Jordi Pun and Kerry Cao
This is a project demonstrating the usage of sockets and IPC's with the classic game Battleship. This game features no GUI and will be played in the CMD line locally over the same network.

### HOW TO PLAY
To start the program run python Battleship.py. This will install all the neccasary dependencies required to play the game. 
You will then be required to enter the opponents Local IP address as well as the the two ports required for the processes to communicate with. 

For example 192.168.1.1 Transmit 8001 Recieve 8000
            192.168.1.2 Transmit 8000 Recieve 8001

The Users will then be required the enter their ship placements and their orientation represented by 0 1 2 3 for right down left up respectively. Coordinates/placement are entered in traditional fashion with Letter followed by a number (A1)

Upon successful conenction players will then take turns firing onto their opponenets board by entering the coordinates. A board will update with a message indicating if they hit a ship or not. 

The game ends when all of a player's ships has sunk or if the player closes the socket.


    
### Dependencies used
    
    netifaces is used to determine the IP of the player to bind to a socket
    numpy is used to initialize the array and for array manipulations
    
    
