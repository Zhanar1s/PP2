import re
text = 'C++ Programs, Python codes.'
print(re.sub("[ ,.]", ":", text))