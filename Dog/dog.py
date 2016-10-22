import math

test_cases = int(input(""))

for x in range(0, test_cases):
    in = input("").split("")
    n = int(in[0])      #number of dogs
    k = int(in[1])      #number of walkers
    size =[]            #size of the dogs

    for i in range(0, n):
        size.append(int(input("")))

    walkGroup = size[0:k]
    for i in range(k, n):
        diff = [math.fabs(w-size[i]) for w in walkGroup]

        #for min diff, kickout
        kickout = walkGroup[min(diff).index()]
        walkGroup[min(diff).index()] = size[i]

        #min knockout
        diff = [math.fabs(w-kickout) for w in walkGroup]
