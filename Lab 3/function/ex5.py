def prime(numbers):
     sorted = []
     for x in numbers:
         for i in range(2,x):
             if x%i==0 :
                 break
         else :
             sorted.append(x)
     return sorted

numbers = map(int ,input().split())
result = prime(numbers)
print(result)