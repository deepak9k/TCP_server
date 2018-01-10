#import the networking file

import socket




#class for the connection as a client
class client(socket.socket):

    def __init__(self):
        socket.socket.__init__(self)

    #To set the fixed rate chunk size
    def msg_size(self,size=10):
        self.size=size

    # Methos to use for sending data
    def send_to_server(self, hostname, port, data):
        self.connect((hostname,port))
        self.send(data.encode('utf-8'))
        self.TR = 0
        self.TS = 0
        self.msg = ""
        while self.TR< self.size:
            rc=self.recv(10)
            self.msg+=rc.decode('utf-8')
            self.TR=len(self.msg)

        return self.msg

    #methd to close the socket
    def cls(self):
        self.close()




if __name__=="__main__":
    #create the object of the client
    c=client()

    #settig the size of the chunk
    c.msg_size()

    #data send to server
    p=c.send_to_server( 'localhost', 80, 'hello_1234')

    #close the conneciton
    c.cls()

    print (p)


