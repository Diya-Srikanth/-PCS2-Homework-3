def sum_3(x):
    x = list(map(int, x.split()))
    for i in range(len(x)):
        for j in range(i):
            for k in range(j):
                if k < j < i and x[i] + x[k] + x[j] == 0:
                    return str(k + 1) + ' ' + str(j + 1) + ' ' + str(i + 1)
    return (-1)


with open("r_3sum.txt", 'r') as file:
    file = file.read()
    f = file.splitlines()
    a = list(map(int, f[0].split()))
    f.remove(f[0])
    for x in f:
        print(sum_3(x))