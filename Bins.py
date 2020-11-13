with open('rosalind_bins.txt','r') as file:
    content = file.read().splitlines()

    c = [int(i) for i in content[2].split()]
    d = [int(j) for j in content[3].split()]
    line=''
    for i in range(len(d)):
        line += str(Binary_search(c, d[i])) + ' '

    print(line)
def number_one(c, d):
    low = 0
    high = len(c)-1
    while low <= high:
        index = (low + high) // 2
        if d == c[index]:
            return index + 1
        elif d > c[index]:
            low = index + 1
        else:
            high = index - 1
    return -1

