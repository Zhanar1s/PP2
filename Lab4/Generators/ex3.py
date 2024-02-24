def genereate_divisible(N):
    for i in range(0, N+1, 12):
        yield i

n = int(input())
for i in genereate_divisible(n):
    print(i, end=" ")
