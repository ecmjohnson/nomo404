tests = int(raw_input(""))
for i in range (0, tests):
    dogs_walkers = raw_input("")
    N = int (dogs_walkers.split(" ")[0])
    K = int (dogs_walkers.split(" ")[1])

    myDawgs = []
    for j in range(0, N):
        myDawgs.append(int (raw_input("")))

    myDawgs.sort(reverse=True)
    flag = True

    walkers = [0]*(N-1)
    for k in range(0,N-1):
        if flag:
            walkers[k] = myDawgs[0]
            del myDawgs[0]
            flag = False
        else:
            walkers[k] = myDawgs[-1]
            del myDawgs[-1]
            flag = True

    walkers.sort(reverse=False)
    while len(myDawgs)>0:
        last_diff = False
        for k in range(0,N-1):
            diff = abs(walkers[k] - myDawgs[0])
            if not last_diff:
                last_diff = diff
            if last_diff < diff:
                walkers[k-1].append(myDawgs[0])
                del myDawgs[0]
                break

    dawg_sizing = 0
    for walker in walkers:
        if isinstance(walker, (int, long)):
            pass
        else:
            dawg_sizing += max(walker) - min(walker)
    print(dawg_sizing)
