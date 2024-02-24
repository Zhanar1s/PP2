def generate_square(a, b):
    for i in range(a, b+1):
        yield pow(i, 2)

x = int(input("Enter a:"))
y = int(input("Enter b:"))
for i in generate_square(x, y):
    print(i, end=" ")


