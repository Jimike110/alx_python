for i in range(1, 100):
    if str(i)[0] == str(i)[-1] and i > 10:
        continue
    elif i > int(str(i)[-1] + str(i)[0]):
        continue
    print("{0:02d}".format(i), end=", " if i < 89 else "\n")