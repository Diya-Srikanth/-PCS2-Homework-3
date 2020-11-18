def par3(f):
    x = f[0]
    less =[]
    equal =[]
    more=[]
    for y in f:
        if y > x:
            more.append(y)
        elif y == x:
            equal.append(y)
        elif y < x:
            less.append(y)
    return less+equal+more

with open("rosalind_par3.txt", "r") as file:
    file = file.read()
    f= list(map(int, file.split()))
    f.remove(f[0])
    result = par3(f)
    print(" ".join(str(t) for t in result))