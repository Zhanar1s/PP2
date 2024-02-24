def Generate(N):
    for i in range (1, N+1):
        yield pow(i, 2)

n = int(input())
for i in Generate(n):
    print(i, end=" ")