for i in range(13):
    if i == 0:
        continue
    elif i == 1:
        continue
    print(i)
    a = 1
    for a in range(13):
        print(i, "*", a, "=", i * a)
        a += 1
    i += 1