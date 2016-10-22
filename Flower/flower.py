def removePetals(x, offset):
    xlen = len(x)

    for i in range(1 + offset, xlen, 2):
        x[i] = -1

    x = list(filter((-1).__ne__, x))

    if(len(x) == 1):
        return(x[0])

    if(xlen % 2):
        return removePetals(x, -1)

    return removePetals(x, 0)

test_cases = int(input(""))

n = [int(input("")) for x in range(test_cases)]

for x in range(0, len(n)):
    print(removePetals([i for i in range(1, n[x]+1)], 0))
