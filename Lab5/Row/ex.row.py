import re
import csv
from tabulate import tabulate

f = open('row.txt', 'r', encoding='utf8')
text = f.read()

pattern = r"\n(?P<sequence>[0-9]+)\.\n(?P<name>.+)\n(?P<quantity>.+)x(?P<price>.+)\n(?P<cost>.+)"

res = re.finditer(pattern, text)

data = []
for x in res:
    data.append([
        x.group('sequence'), 
        x.group('name'),
        float(x.group('quantity').strip().replace(',','.')),
        float(x.group('price').strip().replace(',','.').replace(' ','')),
        float(x.group('cost').strip().replace(',','.').replace(' ',''))
    ])

headers = ['sequence', 'name', 'quantity', 'price', 'cost']
table = tabulate(data, headers=headers, tablefmt='pretty')

with open('formatted_row.txt', 'w', encoding='utf8') as txtfile:
    txtfile.write(table)