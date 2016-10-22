N = int(input(""))

def is_prime(a):
    return all(a % i for i in range(2, a))

primes = []; evac = False;
for i in range(0, N):
    if evac:
        break
    if is_prime(i):
        primes.append(i)
    if len(primes) > 3:
        if N < primes[-1] + primes[-2] + primes[-3]:
            for j in range(0, len(primes)):
                if evac:
                    break
                for k in range(0, j):
                    if evac:
                        break
                    for l in range(0, k):
                        if primes[j] + primes[k] + primes[l] == N:
                            print(str(primes[j]) + ' ' + str(primes[k]) + ' ' + str(primes[l]))
                            evac = True
                            break
