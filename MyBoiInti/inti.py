test_cases = input("")

def rprime(a,b):
    while b: #b != 0
        a,b = b, a%b
    return a == 1

for case in range(0, int(test_cases)):
    temp = input("")
    N = int(temp.split(" ")[0])
    A = int(temp.split(" ")[1])
    B = int(temp.split(" ")[2])

    accum = 0
    for K in range(A, B+1):
        if rprime(N,K):
            accum += K

    print(accum%1000000007)
