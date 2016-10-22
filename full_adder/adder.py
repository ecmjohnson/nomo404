import math

temp = input("")
out1 = temp
base = int(temp.split(" ")[0])
symbols = temp.split(" ")[1]
values = range(0, len(symbols))
mapping = dict(zip(symbols, values))

out2 = input("")
num1 = out2.replace(" ","")
num1_b10_lst = [mapping[a] for a in num1]
out3 = input("")
num2 = out3.replace("+","").replace(" ","")
num2_b10_lst = [mapping[a] for a in num2]

num1_b10_lst = list(reversed(num1_b10_lst))
num1_b10 = sum([int(x*math.pow(base,y)) for x,y in zip(num1_b10_lst, range(0,len(num1_b10_lst)))])
num2_b10_lst = list(reversed(num2_b10_lst))
num2_b10 = sum([int(x*math.pow(base,y)) for x,y in zip(num2_b10_lst, range(0,len(num2_b10_lst)))])

result = num1_b10 + num2_b10

rems = []
last = result
while last != 0:
    Q = math.floor(last/base)
    rems.append(last%base)
    last = Q
rems = list(reversed(rems))

# mapping = dict((v,k) for k,v in mapping.iteritems())
mapping = dict(zip(mapping.values(),mapping.keys()))
num_out = [mapping[a] for a in rems]
print(out1)
print(out2)
print(out3)
print(input(""))
print(' ' + ''.join(num_out))
