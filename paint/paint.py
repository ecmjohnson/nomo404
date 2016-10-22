test_cases = int(input(""))

for x in range(0, test_cases):
    sequence_length = int(input(""))
    sequence = input("").split(' ')
    brush1 = 0
    brush2 = 0
    change = 0

    for i in range(0, sequence_length):
        if(brush1 == sequence[i] or brush2 == sequence[i]):
            pass
        else:
            if(brush1 in sequence[i+1:sequence_length] and brush2 in sequence[i+1:sequence_length]):
                pass
            elif(brush1 in sequence[i+1:sequence_length] and ~(brush2 in sequence[i+1:sequence_length])):
                brush2 = sequence[i]
                change += 1
            elif(~(brush1 in sequence[i+1:sequence_length]) and brush2 in sequence[i+1:sequence_length]):
                brush1 = sequence[i]
                change += 1
            else:
                brush1 = sequence[i]
                change += 1
print(change)
