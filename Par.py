
with open("rosalind_par.txt", 'r') as file:
    file = file.read()
    f= list(map(int,file.split()))
    f.remove(f[0])
    a = f[0]
    c = sorted(f)
    print(" ".join(str(x) for x in c))
