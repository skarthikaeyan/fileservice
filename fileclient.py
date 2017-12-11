import socket
import sys
try:
#try block for KeyboardInterrupt
    try:
#try block for socket error
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host=socket.gethostname()
        port=2000
        s.connect((host,port))

    except socket.error as se:
        print("Can't Connect "+str(se))
        sys.exit()

    fname=raw_input("Enter File name: ")

    while True:

        fname.encode()
        s.send(fname)
        data=s.recv(1024)

        if not data:
            print("File not found, Check spelling(case sensitive)")
            s.close()
            break
        #if data is not returned from the server side it may not be there.
        downfile=open("newfile","wb")

        while data:
            downfile.write(data)
            data=s.recv(1024)
        downfile.close()
        print("Downloaded")
        s.close()
        break

except KeyboardInterrupt as e:
    print("User terminated")
    s.close()
