def solve(numheads, numlegs):
    # x = number of chickens
    # y = number of rabbits

    
    for y in range(numheads + 1):
        x = numheads - y
        if 2 * x + 4 * y == numlegs:
            return x, y

    
    return "No solution"
numheads = int(input())
numlegs = int(input())
result = solve(numheads, numlegs)
print("Number of chickens:", result[0])  
print("Number of rabbits:", result[1])