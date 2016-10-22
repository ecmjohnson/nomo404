## Determinant matrix
def det(m):
    return m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1]) - m[1][0]*(m[0][1]*m[2][2] - m[0][2]*m[2][1]) + m[2][0]*(m[0][1]*m[1][2] - m[0][2]*m[1][1])

#variables
A = [[0, 1, 6], [2, 0, 12], [1, 2, 6]]
Adet = det(A)
isConsistant = 1

y = [int(a) for a in input("").split(" ")]   #mlcl = [C, H, O]
sol = [0]*3

for i in range(0, 3):
    Ai = [row[:] for row in A];
    Ai[0][i] = y[0]
    Ai[1][i] = y[1]
    Ai[2][i] = y[2]

    sol[i] = det(Ai)/Adet

    if(sol[i].is_integer()):
        pass
    else:
        isConsistant = 0
        break

print(sol)

if(isConsistant):
    print(" ".join([str(int(x)) for x in sol]))
else:
    print('Error')
