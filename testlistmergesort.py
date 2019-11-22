if y[0][1] > z[0][1]:  # not subscriptable, 0 is your count not your item
    result.append(z[0])
    z.pop(0)
else:
    result.append(y[0])
    y.pop(0)

result = []
for y_index in y:
    if y_index > z_index:
        result.append(z)
        z.pop()

