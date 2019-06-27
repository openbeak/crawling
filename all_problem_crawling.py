import requests
from bs4 import BeautifulSoup
from db_setting import con


def mainCrawler(proNum, proName, cate, rate):
    try:
        with con.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `app_algoreader` (`problemNum`, `problemName`, `category`, `answerRate`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (proNum, proName, cate, rate))
        con.commit()
        print('DB SAVE SUCCESS')
    except:
        con.rollback()
        print('DB SAVE FAIL')


exceptionProNumArray = []


def exceptProNum():
    try:
        with con.cursor() as cursor:
            # Create a new record
            # sql = "SELECT problemNum FROM algoreader"
            sql = "SELECT problemNum FROM app_algoreader"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for r in rows:
                exceptionProNumArray.append(r[0])
    except:
        con.rollback()
        print('DB SEA FAIL')


exceptProNum()

for page in range(163):
    url_cate = requests.get("https://www.acmicpc.net/problemset/" + str(page + 1))
    soup = BeautifulSoup(url_cate.content, 'html.parser')
    rows = soup.select('tr')
    if rows:
        rows.pop(0)
        pro = {}
        for r in rows:
            proNum = int(r.select('td')[0].getText())
            if proNum in exceptionProNumArray:
                exceptionProNumArray.remove(proNum)
            else:
                proName = r.select('td')[1].getText()
                cate = 'None'
                rate = int(float(r.select('td')[5].getText()[:-1])*100)
                print(proNum, proName, cate, rate)
                mainCrawler(proNum, proName, cate, rate)

con.close()
