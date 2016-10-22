import math

test_cases = int(input(""))

for x in range(0, test_cases):
    info = input("").split(" ")
    p = int(info[0]); s = int(info[1]); n = int(info[2]);
    addresses = []
    FIFOcount = 0
    LRUcount = 0

    for j in range(0, n):
        addresses.append(int(input("")))

    page = [math.floor(a/s) for a in addresses]

    FIFO = []
    LRU = []
    stack = []

    for i in range(0, n):
        #FIFO
        if(page[i] in FIFO):
            pass
        else:
            if(len(FIFO) < p):
                FIFO.append(page[i])
                stack.append(page[i])
            else:
                FIFO[FIFO.index(stack[0])] = page[i]
                stack.pop(0)
                stack.append(page[i])
                FIFOcount += 1

        #LRU
        if(page[i] in LRU):
            if(LRU.index(page[i]) != p):
                LRU.remove(LRU.index(page[i]))
                LRU.append(page[i])
        else:
            LRU.append(page[i])
            if(len(LRU) > p):
                LRU.pop(0)
                LRUcount+=1

    if(LRUcount < FIFOcount):
        print("yes " + str(FIFOcount) + " " + str(LRUcount))
    else:
        print("no " + str(FIFOcount) + " " + str(LRUcount))
