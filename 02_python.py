a = int(input(""))
b = {}
count = 0
c = []
for i in range(0,a):
    key = input("")
    if b.get(key):
        b[key] += 1
    else:
        b[key] = 1
        count += 1
        c.append(key)

print(count)
for key in c:
    print(b[key], end =" ")
