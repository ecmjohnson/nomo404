import math

temp = input("")
base = int(temp.split(" ")[0])
symbols = temp.split(" ")[1]
values = range(0, len(symbols))
mapping = dict(zip(symbols, values))
print(mapping)

num1 = input("").replace(" ","")
num1_b10_lst = [mapping[a] for a in num1]
num2 = input("").replace("+","").replace(" ","")
num2_b10_lst = [mapping[a] for a in num2]

num1_b10_lst = list(reversed(num1_b10_lst))
num1_b10 = sum([int(x*math.pow(base,y)) for x,y in zip(num1_b10_lst, range(0,len(num1_b10_lst)))])
num2_b10_lst = list(reversed(num2_b10_lst))
num2_b10 = sum([int(x*math.pow(base,y)) for x,y in zip(num2_b10_lst, range(0,len(num2_b10_lst)))])

result = num1_b10 + num2_b10
