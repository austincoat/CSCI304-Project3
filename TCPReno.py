import time
import threading
seqnum = 1
acknum = 0
payload = []
windowSize = 1
seqnumClient = 0
count = 0
maxWindowSize = 8

timeStamp =[]


def send(seqnumS,payloadS,windowSizeS):
    global windowSize
    global count
    while (True):
        if( acknum == payloadS):
            break
        if (count+1 == payloadS):
            timeStamp.append(seqnumS)
            timeStamp.append("sent")
            timeStamp.append(time.time())
            client(payloadS,seqnumS)
            seqnumS = seqnumS + 1
            time.sleep(1)

            #print acknum
        while (acknum < seqnumClient):
            print "waiting"


def ackReceive(seqnumC):
    global acknum
    global windowSize
    global count
    global maxWindowSize
    count = count + 1
    acknum= acknum+1
    timeStamp.append(seqnumC)
    timeStamp.append("rec")
    timeStamp.append(time.time())
    if(acknum == windowSize):
        windowSize = windowSize + windowSize


        # if(windowSize == maxWindowSize):
        #     windowSize = windowSize/2
        print windowSize
        time.sleep(2)


def client(payloadC,seqnumC):

    global seqnumClient
    tempseqnumClient = seqnumClient + 1
    if (tempseqnumClient == seqnumC):
        ackReceive(seqnumC)
        seqnumClient= seqnumClient +1
        #print seqnumClient

def main():
    seqnumClient = 0
    for i in range(10):
        payload.append(i+1)

    i= 0
    temp = 1
    while(acknum <10):
        if(i<10):
            t1 = threading.Thread(target=send, args = (seqnum,payload[i],windowSize))
            t1.daemon = True
            print "send"
            t1.start()
            temp = temp +1
            i = i+1


    for k in range(len(timeStamp)):
        print timeStamp[k]




    #send(seqnum,payload,windowSize)


main()
