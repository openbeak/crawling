import requests
from bs4 import BeautifulSoup
import sys

#
# reload(sys)
# sys.setdefaultencoding('utf-8')

problem_num = 1000

res = requests.get('https://www.acmicpc.net/problem/tags')
soup = BeautifulSoup(res.content, 'html.parser')

problem_category = []
category_count = 0
over_10_category = 0
over_40_category = 0
over_80_category = 0

tags = soup.findAll('tr')

tags.pop(0)

for c in tags:
    name = c.select('td')[0].getText()
    count = c.select('td')[1].getText()
    problem_category.append(name)
    category_count += 1
    if int(count) > 10:
        over_10_category += 1
    if int(count) > 40:
        over_40_category += 1
    if int(count) > 80:
        over_80_category += 1

print("category_count : " + str(category_count))
print("category_count_over_10 : " + str(over_10_category))
print("category_count_over_40 : " + str(over_40_category))
print("category_count_over_80 : " + str(over_80_category))
