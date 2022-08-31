path = 'out_10000.txt'

f = open(path, encoding="UTF-8")

obj = eval(f.read())

f.close()

result = 0

for elem in obj :
    result += elem[1]

print(result)