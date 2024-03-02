def string_test(s):
    upper=0
    slower=0

    for i in s:
        if i.isupper():
            upper+= 1
        elif i.islower():
            slower+= 1
        else:
            pass
    return upper, slower
s=input()
upper,slower=string_test(s)
print("Numbers of upper:", upper)
print("Numbers of slower:", slower)

