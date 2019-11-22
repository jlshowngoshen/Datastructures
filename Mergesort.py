def msort(x):
    result = []
    print("result", result)
    if len(x) < 2:
        return x
    mid = int(len(x) // 2)
    print("mid", mid)
    y = msort(x[:mid])
    z = msort(x[mid:])
    print("ymsort", y)
    print("zmsort", z)
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:

            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)


        elif len(y) > 0:

            for i in y:
                result.append(i)
                y.pop(0)
            else:
                for i in y:
                    result.append(i)
                    y.pop(0)

    return result


def printList(x):
    for i in range(len(x)):
        print(x[i], end=" ")


print()

if __name__ == '__main__':
    x = [22, 13, 45, 61]
    print("Given array is", end="\n")
    printList(x)
    print()
    print("Sorted array is: ", end="\n")
    printList(x)
# x = [22, 13, 45, 61]
# msort(x)
# print()



