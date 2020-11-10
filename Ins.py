if __name__ == '__main__':
    a = input()
    b = list(map(int, input().split()))
    c=0
    for i in range(len(b)):
        if i == 0:
            continue
        for j in range(0,i):
            if b[j] > b[i]:
                temp = b[j]
                b[j] = b[i]
                b[i] = temp
                c+=1
    print (c)
