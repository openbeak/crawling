import requests
from bs4 import BeautifulSoup
from db_setting import con


def mainCrawler(proNum, proName, cate, rate):
    try:
        with con.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `app_total_problems` (`problemNum`, `problemName`, `category`, `answerRate`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (proNum, proName, cate, rate))
        con.commit()
        print('DB SAVE SUCCESS')
    except:
        con.rollback()
        print('DB SAVE FAIL')


problem_category = []

res = requests.get('https://www.acmicpc.net/problem/tags')
soup = BeautifulSoup(res.content, 'html.parser')

tags = soup.findAll('tr')
tags.pop(0)

for c in tags:
    name = c.select('td')[0].getText()
    count = c.select('td')[1].getText()
    problem_category.append(name)

for c in problem_category:
    url_cate = requests.get('https://www.acmicpc.net/problem/tag/' + c)
    soup = BeautifulSoup(url_cate.content, 'html.parser')
    print("cate - " + c)
    cate_length = len(soup.select('.pagination li'))
    print(cate_length)
    for page in range(cate_length):
        url_cate = requests.get('https://www.acmicpc.net/problem/tag/' + c + "/" + str(page + 1))
        soup = BeautifulSoup(url_cate.content, 'html.parser')
        rows = soup.select('tr')
        if rows:
            rows.pop(0)
            pro = {}
            for r in rows:
                proNum = int(r.select('td')[0].getText())
                proName = r.select('td')[1].getText()
                cate = c
                rate = r.select('td')[5].getText()
                submitCount = int(r.select('td')[0].getText())
                print(proNum, proName, cate, rate, submitCount)
                mainCrawler(proNum, proName, cate, rate, submitCount)

con.close()
