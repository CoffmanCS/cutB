#Prints out Inputted number of layers of Pascal's Triangle.

r = int(input("How many layers: "))

x = []
finals=[]
for i in range(r):
    x.insert(0,1)
    for z in range(len(x)-1):
        x[z] = x[z] + x[z + 1]
    y = [1]
    [y.append(v) for v in x]
    finals.append(" ".join([str(v) for v in y]))
# [print(len(finals[i])) for i in range(len(finals)-1)]
[print(i) for i in finals]

input("Press enter to exit Program: ")


for i in range(5):
    print("Hello")