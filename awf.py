a = int(input("Enter a number: "))
c = a % 10
flag = "YES"

original_a = a  # Store the original value of a

while a > 0:
    digit = a % 10
    if digit > c:
        flag = "NO"
    a //= 10

print(flag)
