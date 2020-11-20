def inv(arr):
    inversions = 0
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a, ai = inv(a)
        b, bi = inv(b)
        c = []
        i = 0
        j = 0
        inversions = ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions

if __name__ == "__main__":
    with open("rosalind_inv.txt", "r") as f:
        n = int(f.readline().strip())
        A = [int(i) for i in f.readline().strip().split()]
    arr, inv_count = inv(A)
    print(inv_count)
