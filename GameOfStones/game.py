test_cases = int(input(""))

for t in range(0, test_cases):
    nGames = int(input(""))
    games = [0]*nGames
    nTurns = [0]*nGames

    for i in range(0, nGames):
        nStones = int(input(""))
        games[i] = [int(x) for x in input("").split(" ")]
        nTurns[i] = sum([(a-1)/2 for a in games[i]])

    totalTurns = sum(nTurns)

    if(totalTurns % 2): #odd case
        print("Alice")
    else:
        print("Bob")
