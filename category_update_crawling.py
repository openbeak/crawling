import requests
from bs4 import BeautifulSoup
from db_setting import con


def mainCrawler(mock_data):
    try:
        with con.cursor() as cursor:
            sql = "UPDATE `all_baek` SET category = %s WHERE problemNum = %s"
            # cursor.execute(sql, (cate, proNum))
            cursor.executemany(sql, mock_data)
        con.commit()
        print('DB UPDATE SUCCESS')
    except:
        con.rollback()
        print('DB UPDATE FAIL')


# test_db = []
# test_db.append(("구현", 1000))
# test_db.append(("구현", 1001))

problem_category = []
res = requests.get('https://www.acmicpc.net/problem/tags')
soup = BeautifulSoup(res.content, 'html.parser')

tags = soup.findAll('tr')
tags.pop(0)

for c in tags:
    name = c.select('td')[0].getText()
    count = c.select('td')[1].getText()
    problem_category.append(name)

test_db = []

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
                print(proNum, proName, cate, rate)
                test_db.append((cate, proName))

mainCrawler(test_db)
con.close()

# update crawling 작동이 안된다.
