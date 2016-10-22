tests = int(raw_input(""))
for i in range (0, tests):
    dogs_walkers = raw_input("")
    N = int (dogs_walkers.split(" ")[0])
    K = int (dogs_walkers.split(" ")[1])

    myDawgs = []
    for j in range(0, N):
        myDawgs.append(int (raw_input("")))

    myDawgs.sort(reverse=True)

    # original divying up of dogs
    walkers = [0]*(N-1)
    for k in range(0,N-1):
        walkers[k] = myDawgs[0]
        del myDawgs[0]

    # extra dogs must get owners
    for i in range(0, len(myDawgs)):
        diffs = []
        for j in range(0, len(walkers)):
            pass
