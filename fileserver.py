import sys
import socket
import os
try:
#this try block is for key board KeyboardInterrupt
    try:
#this try block is for socket error
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #reuse the address in case the connection is not closed properly
        host=socket.gethostname()
        port=2000
        sock.bind((host,port))
        print("Server started")
        sock.listen(10)
        print("Waiting for connection")
        found=0

        while True:
            data,addr=sock.accept()
            print("Connected to"+str(addr))
            fname=data.recv(1024)

            for file in os.listdir("workspace/"):
                #listdir is used to return the file list in mentioned directory
                if file==fname:
                    print(fname+" found.")
                    found=1
                    upfile=open("workspace/"+fname,"rb")
                    a=upfile.read(1024)

                    while True:
                        data.send(a)
                        a=upfile.read(1024)
                        if not a:
                            print("File sent")
                            upfile.close()
                            data.close()
                            sock.close()
                            sys.exit()

        if found==0:
            print(fname+" not Found..")
            data.close()
            sock.close()
            break

except socket.error as se:
    print(str(se))
    sys.exit()

except KeyboardInterrupt as e:
    print("User terminated")
    sock.close()
    sys.exit()
