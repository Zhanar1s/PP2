elements = ['реті\n', 'аты\n', 'саны\n', 'бағасы\n', 'кұны\n']

# Write to the file
with open('row.txt', 'w', encoding='utf-8') as fw:
    fw.writelines(elements)

# Read from the file
with open('row.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        print(line, end='')
