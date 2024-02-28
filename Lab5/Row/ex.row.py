import re
import csv
from tabulate import tabulate

f = open('row.txt', 'r', encoding='utf8')
text = f.read()

pattern = r"\n(?P<реті>[0-9]+)\.\n(?P<аты>.+)\n(?P<саны>.+)x(?P<бағасы>.+)\n(?P<құны>.+)"

res = re.finditer(pattern, text)

data = []
for x in res:
    data.append([
        x.group('реті'), 
        x.group('аты'),
        float(x.group('саны').strip().replace(',','.')),
        float(x.group('бағасы').strip().replace(',','.').replace(' ','')),
        float(x.group('құны').strip().replace(',','.').replace(' ',''))
    ])

headers = ['реті', 'аты', 'саны', 'бағасы', 'құны']
table = tabulate(data, headers=headers, tablefmt='pretty')

with open('formatted_row.txt', 'w', encoding='utf8') as txtfile:
    txtfile.write(table)
