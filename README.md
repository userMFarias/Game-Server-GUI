# Game-Server-GUI

Socket programming
You are required to write two programs (client andserver) in Python, that implement the game1 described below. The game is between two instances of the client who play against each other using the server2. Each player sends an integer between 0 and 9; if the two numbers differ by 3 or less, the player who sent the higher number wins; instead, if the two numbers differ by 4 or more, the player who sent the lower number wins. If the two numbers are equal, there is a draw. All messages have to be sent/received using the TCP protocol.
Client
The client has to be coded according to the following specification.
•	At startup, the client prompts for an integer number I between 0 and 9 from the user.
•	The client connects to the server (via TCP) and sends I; then it listens for an integer N which can be 0, 1 or 2.
•	Upon receiving N, the client prints “You win!” if N = 1, “You lose!” if N = 0, or “Draw!” if N = 2.
•	Finally, the client disconnects from the server.

Server
The server has to be coded according to the following specification.
•	The server waits for connections.
•	Once two connections are established upon request of the clients (say Client 1 and Client 2), the server waits for integer numbers I1 and I2 from Client 1 and Client 2, respectively.
•	The server receives I1 and I2 from Client 1 and Client 2, respectively, in any order.
•	The server determines the winner as follows. If the two numbers are equal, there is a draw. If the two numbers differ by 3 or less, the player who sent the
higher number wins; instead, if the two numbers differ by 4 or more, the player who sent the lower number wins.
•	If there is a draw, the server sends the integer 2 to both clients; otherwise, it sends the integer 1 to the winner client and 0 to the loser client.

1The game is not intended to be interesting or entertaining; it serves mainly for this coding exercise. However, you can try and play it.
2In principle the server could allow several games in parallel, each played by a pair of client instances, but for the purpose of this assignment the server is only required to manage one game at a time.
 
Further instructions
1.	The programs do not need to be robust to errors. For example, you can assume that the user enters numbers between 0 and 9, that the messages are sent in the right order etc.
2.	The Python code for the client and the server, as above specified, is to be submitted as two Python files.
3.	You must produce a brief, informal description of the code in the relevant section of the PDF file of your submission. The description needs to include
screenshots of three executions, two of the client and one of the server, where the two clients play one match of the described game. One screenshot per each instance (one server and two clients) are sufficient, if the messages all fit in the window; you are obviously allowed to add additional messages with respect to those in the specification, which might help for debugging.

Open the server, start the server.
The server waits for the 2 clients to connect. 
Once connected they are asked to send a number, if the number is equal, it is a draw. If the numbers differ by 3 or less the higher number winds. If the numbers differ by 4 or more, the lower number wins.
