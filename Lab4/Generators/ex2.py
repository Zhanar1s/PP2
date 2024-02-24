def even_generate(N):
    for i in range(0, N+1, 2):
        yield i

n = int(input())
even_numbers = even_generate(n)
print(*even_numbers, sep=',')

