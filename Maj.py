with open("rosalind_maj.txt", "r") as file:
    k, n = map(int, file.readline().strip().split())
    a = [line.strip().split() for line in file]

for i in range(k):
    c = [a[i].count(a[i][j]) > n/2 for j in range(n)]
    if any(c):
        print(a[i][c.index(True)], end=" ")
    else:
        print("-1", end=" ")
