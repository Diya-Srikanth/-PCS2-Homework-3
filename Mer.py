with open('rosalind_mer.txt', 'r') as file:
    content = file.read()
    content = content.strip(' ').split('\n')
    l=[]
    for i in range(len(content)):
        if i%2 !=0:
            a=list(map(int,content[i].split()))
            for x in a:
                l.append(x)
                l = sorted(l)
    print(' '.join([str(x) for x in l]))
