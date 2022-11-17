import socket
from function.response import *

def getRequest(connection):
    request = ""
    connection.settimeout(1)
    try:
        # Receive request
        request = connection.recv(1024).decode()
        while (request):
            request += connection.recv(1024).decode()
    except socket.timeout:
        # If timeout
        if not request:
            print("--------------------\n[SERVER]\nNo request from client\n")
    finally:
        # Parse the request
        return RequestParse(request)


class RequestParse:
    def __init__(self, request):
        requestArray = request.split("\n")
        if request == "":
            self.empty = True	# If there is no request content
        else:
            self.empty = False
            self.method = requestArray[0].split(" ")[0]		# GET method
            self.path = requestArray[0].split(" ")[1]		# GET path
            self.content = requestArray[-1]					# GET request content

# GET Method
def getMethod(connection, request):
    open("login.txt", "w").write("GET")
    connection.sendall(Response(request.path).transferFile())
    print("--------------------\n[SERVER]\nRequest %s with path %s DONE\n"%(request.method, request.path))

# POST Method
def postMethod(connection, request):
    if(request.content == "uname=admin&psw=123456&remember=on"):
        open("login.txt", "w").write("POST")
        connection.sendall(Response(request.path).transferFile())
    else:
        requestPath = "/401.html"
        connection.sendall(Response(requestPath).transferFile())
    print("--------------------\n[SERVER]\nRequest %s with path %s DONE\n"%(request.method,request.path))

