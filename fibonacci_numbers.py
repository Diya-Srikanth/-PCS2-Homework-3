if __name__ == '__main__':
    a = int(input())
    l = [0,1]
    for i in range(0, a+1):
        if i >= 2 :
            y = l[-1] + l[-2]
            l.append(y)
    print (l[-1])











