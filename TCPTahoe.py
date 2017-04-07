import time
import threading

seqNum = []
payload = []
ackNum = 0
windowSize= 1
windowReset =0
timeStamp =[]
sendTemp = 0



def send(seqNumS,payloadS,windowSizeS):
    global ackNum
    global sendTemp
    global windowSize
    if(0 == seqNumS % 10 and windowSizeS != -1):
        print "lost"
        windowSize = 1
        timeStamp.append(seqNumS)
        timeStamp.append("sent")
        timeStamp.append(time.time())
        client(seqNumS,"lost")
        client(seqNumS,payloadS)
    else:
        timeStamp.append(seqNumS)
        timeStamp.append("sent")
        timeStamp.append(time.time())
        client(seqNumS,payloadS)

def client(seqNumC,payloadC):
    if(payloadC == "lost"):
        time.sleep(3)
        return seqNumC
    time.sleep(1)
    ackRec(seqNumC)

def ackRec(seqNumA):
    global ackNum
    global windowSize
    global windowReset

    #this will keep printing 4 if 5 gets lost
    if(ackNum == seqNumA - 1):
        ackNum = seqNumA
        #print ackNum
    #ackNum = ackNum + 1

    windowReset = windowReset + 1

    timeStamp.append(seqNumA)
    timeStamp.append("Rec")
    timeStamp.append(time.time())

    increase = 1
    if(windowSize <8):
        increase = windowSize

    if(windowReset == windowSize):
        windowSize = windowSize + increase
        print "testst"
        windowReset = 0


    #print windowSize
    print seqNumA

def main():
    f = open('file.txt', 'wb')
    global payload
    global seqNum
    global windowSize
    global ackNum

    for i in range(50):
        seqNum.append(i+1)
        payload.append(i+1)


    for k in range(50):
        time.sleep(1)

        t1 = threading.Thread(target=send, args = (seqNum[k],payload[k],windowSize))
        t1.daemon = True
        t1.start()

    for k in range(len(timeStamp)):
        f.write(str(timeStamp[k]))
        f.write("\n")
        print timeStamp[k]



    #send(seqnum,payload,windowSize)


main()
