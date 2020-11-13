with open("ms.txt", 'r') as file:
    file = file.read()
    f = list(map(int, file.split()))
    a = int(f[0]) // 2
    f.remove(f[0])
    first = f[:a]
    one = sorted(first)
    second = f[a:]
    two = sorted(second)
    b = one + two
    x = sorted(b)
    print(" ".join(str(y) for y in x))
