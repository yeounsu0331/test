a = 0
b = 1

for i in range(10):
    for j in range(10):
        print("{}*{}={}".format(a, b, a*b))
        b = b + 1
    a = a + 1
    b = 1
    print()