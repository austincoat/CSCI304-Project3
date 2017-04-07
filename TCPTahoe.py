import time
import threading

seqNum = []
payload = []
ackNum = 0
windowSize= 1
windowReset =0

def send(seqNumS,payloadS,windowSizeS):
    global ackNum

    while(windowSizeS <= ackNum):
        print ""

    client(seqNumS,payloadS)



def client(seqNumC,payloadC):
    ackRec(seqNumC)



def ackRec(seqNumA):
    global ackNum
    global windowSize
    global windowReset
    ackNum = ackNum + 1
    windowReset = windowReset + 1


    if(windowReset == windowSize):
        windowSize = windowSize + windowSize
        print "testst"
        windowReset = 0
        ackNum = 0


    #print windowSize
    print seqNumA



def main():
    global payload
    global seqNum
    global windowSize

    for i in range(25):
        seqNum.append(i+1)
        payload.append(i+1)

    for k in range(25):
        t1 = threading.Thread(target=send, args = (seqNum[k],payload[k],windowSize))
        t1.daemon = True
        t1.start()



    #send(seqnum,payload,windowSize)


main()
