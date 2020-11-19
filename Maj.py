def maj(f,a):
    for x in f:
        if f.count(x)>a/2:
            return x
    return(-1)
            
with open("rosalind_maj.txt", "r") as file:
    file = file.read()
    f = file.splitlines()
    l=[]
    a = list(map(int, f[0].split()))
    f.remove(f[0])
    for i in range(a[0]):
        f[i] = list(map(int, f[i].split()))
        p = (maj(f[i],a[1]))
        l.append(p)
    print(" ".join(str(x) for x in l))
        
