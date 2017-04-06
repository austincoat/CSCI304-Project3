import threading
seqnum = 1
acknum = 0
payload = []
windowSize = 1
seqnumClient = 0
count = 0




def send(seqnumS,payloadS,windowSizeS):
    global windowSize

    while (True):

        if( acknum == len(payloadS)):
            break;
        elif (count+1 == payload[count]):
            client(payloadS[count],seqnumS)
            seqnumS = seqnumS + 1
        while (acknum < seqnumClient):
            print "waiting"


def ackReceive():
    global acknum
    global windowSize
    global count
    count = count + 1
    acknum= acknum+1

    #print acknum




def client(payloadC,seqnumC):

    global seqnumClient
    tempseqnumClient = seqnumClient + 1
    if (tempseqnumClient == seqnumC):
        ackReceive()
        seqnumClient= seqnumClient +1
        print seqnumClient
    else:
        count = tempseqnumClient

def main():
    seqnumClient = 0
    for i in range(10):
        payload.append(i+1)
    t1 = threading.Thread(target=send, args = (seqnum,payload,windowSize))
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=send, args = (seqnum,payload,windowSize))
    t2.daemon = True
    t2.start()
    t3 = threading.Thread(target=send, args = (seqnum,payload,windowSize))
    t3.daemon = True
    t3.start()


    #send(seqnum,payload,windowSize)


main()
