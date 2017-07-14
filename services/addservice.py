# server.py 
import socket                                         
import time

def addnumbers(num1, num2):
    return num1*num2

def getparams(data):
    param_string = data.split("\n")[2]
    params = param_string.split("&")
    
    arr = []
    for param in params:
        arr.append(int(param.split("=")[1]))
    return arr
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "localhost" #socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      
    
    print("Got a connection from %s" % str(addr))
    data = clientsocket.recv(1024)
    
    print(data) #.split("\n"))
    params = getparams(data)
    
    if not(len(params)==2):
        resp = "Parameter length doesn't match"
    else:
        resp = str(addnumbers(params[0],params[1]))
    
    clientsocket.send(resp)
    clientsocket.close()
