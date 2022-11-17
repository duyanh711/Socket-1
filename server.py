import socket
import threading
from function.parseMethod import *

# Define socket host and port
HOST = '127.0.0.1'
PORT = 8080
allThreadClients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)
print("--------------------\n[SERVER]\nListening on port %s ..." % PORT)

def handleClient(connection):
    while True:
        request = getRequest(connection)
        if(not request.empty):
            # Send HTTP response
            if(request.method == "GET"):
                getMethod(connection, request)
            if(request.method == "POST"):
                postMethod(connection, request)
            print("--------------------\n[SERVER]\nRequest DONE")   

def Main():
    # activeClient = 1
    # for server in listSocket:
    #     thread = threading.Thread(target=handleClient, args=())
    #     print("--------------------\n[SERVER]\nClient %d: Connected"%(activeClient))
    #     activeClient = activeClient + 1
    #     thread.start()
    #     allThreadClients.append(thread)
    # for thread in allThreadClients:
    #     thread.join()
    while True:
        connection, address = server.accept()
        print(connection)
        thread = threading.Thread(target=handleClient, args=(connection,))
        thread.start()
        allThreadClients.append(thread)
    
    for thread in allThreadClients:
        thread.join()
    server.close()

if(__name__ == "__main__"):
    Main()