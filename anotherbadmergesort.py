def msort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    print('x', x)
    print("len", len(x))
    print("intlenx", int(len(x)/ 2))
    print("mid", mid)
    y = msort(x[:mid])
    print("x[:mid]", (x[:mid]))
    z = msort(x[mid:])
    print("ymsort", y)
    print("zmsort", z)
    print(y) and print(z)
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
## You could use enumerate instead
# or use list comprehension, [ expression for item in list if conditional ]
            if y[0][1] > z[0][1]:  # not subscriptable, 0 is your count not your item
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
##
        elif len(z) > 0:
            print('z', z)
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                print("rap", result.append(i))
                y.pop(0)
    return result


x = [22, 13, 45, 61]
msort(x)
