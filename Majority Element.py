with open("rosalind_maj.txt", "r") as file:
    k, n = map(int, file.readline().strip().split())
    A = [line.strip().split() for line in file]

for i in range(k):
    c = [A[i].count(A[i][j]) > n/2 for j in range(n)]
    if any(c):
        print(A[i][c.index(True)], end=" ")
    else:
        print("-1", end=" ")
