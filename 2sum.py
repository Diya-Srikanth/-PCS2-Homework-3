def sum_2(x):
    b = list(map(int, x.split()))
    for i in range(len(b)):
        for j in range(i):
            if j<i and b[j] == -b[i]:
                return str(j+1)+" "+str(i+1)
    return(-1)
with open('rosalind_2sum.txt', 'r') as file:
    file = file.read()
    f = file.splitlines()
    a = f[0].split()
    f.remove(f[0])
    for x in f:
        print(sum_2(x))