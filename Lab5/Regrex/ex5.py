import re
def text_match(text):
        patterns = '^a.*?(b)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))