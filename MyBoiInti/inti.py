test_cases = input("")

def rprime(a,b):
    while b: #b != 0
        a,b = b, a%b
    return a == 1

def coprimen(N,A,B):
    n = B
    while n > A-1:
       if rprime(N, n):
           yield n
       n = n - 1

for case in range(0, int(test_cases)):
    temp = input("")
    N = int(temp.split(" ")[0])
    A = int(temp.split(" ")[1])
    B = int(temp.split(" ")[2])

    print(sum(coprimen(N,A,B))%1000000007)
