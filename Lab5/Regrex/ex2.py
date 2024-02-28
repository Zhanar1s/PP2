import re
def text_match(text):
        patterns = 'ab{3,4}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("aaaabbbbbbbbbbbbb"))
print(text_match("aabbbbbc"))