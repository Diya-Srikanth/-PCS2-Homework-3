with open("rosalind_med.txt", "r") as file:
    file = file.read()
    f = list(map(int, file.split()))
    a = f[0]
    f.remove(f[0])
    b = f[-1]
    f.pop()
    l = sorted(f)
    print(l[b - 1])
