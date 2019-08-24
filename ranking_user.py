import requests
from bs4 import BeautifulSoup
import user_solving_number

import json

result = []
count = 0

for page in range(10):
    res = requests.get("https://www.acmicpc.net/ranklist/"+str(page))
    soup = BeautifulSoup(res.content, 'html.parser')
    user_id_list = soup.select('td:nth-child(2)')

    for user_id in user_id_list:
        user_id_string = user_id.getText()
        print(str(count)+" : "+user_id_string)
        count += 1
        one_user_solving_list = user_solving_number.crawling_user_num(user_id_string)
        one_result = {}
        one_result['user_id'] = user_id_string
        one_result['rank'] = count
        one_result['solving_problem'] = one_user_solving_list
        json_one = json.dumps(one_result)
        result.append(json_one)
    

with open("ranker.json", "w") as outfile:
    json.dump(result, outfile)



