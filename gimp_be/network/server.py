#runs remote to read file create by server or other program or script
def runRemote():
    global function_parameters
    function_parameters.extend(('runRemote','null'))
    import os, sys
    from time import sleep
    from os import listdir
    from os.path import isfile, join
    from time import sleep         
    pathname =os.path.dirname(sys.argv[0])
    mypath=pathname   
    try:
        for x in range(0,60):
            #look for remote.py
            doLog("runRemote() running in "+os.getcwd())
            if 'Kodkod' in os.getcwd():
                if os.path.isfile("remote.py"):
                    execfile("remote.py")
                    doLog('runRemote() -file executed')
                    os.remove("remote.py")
                    doLog('runRemote() -file deleted')
            else:
                if os.path.isfile("remote1.py"):
                    execfile("remote1.py")
                    doLog('runRemote() -file executed')
                    os.remove("remote1.py")
                    doLog('runRemote() -file deleted')
            #wait 7 seconds
            sleep( 7 )
    except KeyboardInterrupt:
        pass


#reads udp message sent from phone app
def readPhoneSensor(ip_addr):
    UDP_IP = ip_addr
    UDP_PORT = 55007
    doLog("readPhoneSensor("+UDP_IP+") Receiver Port: ", UDP_PORT)
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    return "received message: ", "%1.4f" %unpack_from ('!f', data, 0), "%1.4f" %unpack_from ('!f', data, 4), "%1.4f" %unpack_from ('!f', data, 8), "%1.4f" %unpack_from ('!f', data, 12),"%1.4f" %unpack_from ('!f', data, 16), "%1.4f" %unpack_from ('!f', data, 20), "%1.4f" %unpack_from ('!f', data, 24), "%1.4f" %unpack_from ('!f', data, 28),"%1.4f" %unpack_from ('!f', data, 32), "%1.4f" %unpack_from ('!f', data, 36), "%1.4f" %unpack_from ('!f', data, 40), "%1.4f" %unpack_from ('!f', data, 44), "%1.4f" %unpack_from ('!f', data, 48), "%1.4f" %unpack_from ('!f', data, 52), "%1.4f" %unpack_from ('!f', data, 56), "%1.4f" %unpack_from ('!f', data, 60), "%1.4f" %unpack_from ('!f', data, 64), "%1.4f" %unpack_from ('!f', data, 68), "%1.4f" %unpack_from ('!f', data, 72), "%1.4f" %unpack_from ('!f', data, 76), "%1.4f" %unpack_from ('!f', data, 80), "%1.4f" %unpack_from ('!f', data, 84), "%1.4f" %unpack_from ('!f', data, 88), "%1.4f" %unpack_from ('!f', data, 92)

