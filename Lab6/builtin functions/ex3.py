def isPalindrome(string):
    restr = string.upper()[::-1]
    return restr == string.upper()

string = input()
print(isPalindrome(string))
