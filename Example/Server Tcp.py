import socket


#class for the server
class server(socket.socket):



    def __init__(self):
        # socket creation in the __init__ function

        socket.socket.__init__(self)

        # Size of chunk
    def msg_size(self,size=10):
        self.size=size

    #start the server
    def start_server(self):

        #first bind the socket to host address
        self.bind(('localhost',80))

        # start listen
        self.listen()

        #Accept the client
        c,addr=self.accept()

        while True:
            dmsg = ""
            TR = 0

            #loop to check the chunk size
            while TR<self.size:
                #recv msg from the client
                msg=c.recv(10)
                dmsg+=msg.decode('utf-8')
                TR=len(dmsg)

            # Print the msg received
            print(dmsg)

            #input by server user
            w=input()

            # data encoded in the byte object
            EW=w.encode('utf-8')

            #send the data to the client

            print (EW)
            c.send(EW)



if __name__=="__main__":


    #create the sever object
    s=server()

    #define the size of chunk(default :- 10 character)
    s.msg_size()

    #start the server
    s.start_server()