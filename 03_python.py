def get_div(n):
    c = []
    for e in range(1,n+1):
        if n%e==0:
            c.append(e)
    return c

def get_common_div(a, b):
    c = []
    for i in range (0, len(a)):
        if is_in(b, a[i]):
            c.append(a[i])
    return c

def is_in(l, elem):
    for j in range (0, len(l)):
        if l[j] == elem:
            return True
    return False


# main
a, b = map(int,input("Enter a number:").split())
divisors = get_common_div(get_div(a), get_div(b))
for d in divisors:
    print(d, end = " ")
