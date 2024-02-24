def generate_returns(N):
    for i in range(N, -1, -1):
        yield i

n = int(input())
numbers = generate_returns(n)
print(*numbers, sep=", ")