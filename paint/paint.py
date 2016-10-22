test_cases = int(input(""))

for x in range(0, test_cases):
    sequence_length = int(input(""))
    sequence = input("").split(' ')
    brush1 = 0
    brush2 = 0
    change = 0

    for i in range(0, sequence_length):
        subsequence = sequence[i+1:sequence_length]

        if(brush1 == sequence[i] or brush2 == sequence[i]):
            pass
        else:
            if(brush1 in subsequence and brush2 in subsequence):
                if(subsequence.index(brush1) > subsequence.index(brush2)):
                    brush1 = sequence[i]
                else:
                    brush2 = sequence[i]
            elif(brush1 in subsequence and ~(brush2 in subsequence)):
                brush2 = sequence[i]
            elif(~(brush1 in subsequence) and brush2 in subsequence):
                brush1 = sequence[i]
            else:
                brush1 = sequence[i]

            change += 1

        print(change)
