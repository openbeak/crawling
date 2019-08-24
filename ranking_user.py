import requests
from bs4 import BeautifulSoup
import user_solving_number
import random
import json

result = []


pagerange = random.sample(range(1, 551), 10)

for page in pagerange:
    res = requests.get("https://www.acmicpc.net/ranklist/"+str(page))
    soup = BeautifulSoup(res.content, 'html.parser')
    user_id_list = soup.select('tr')
    user_id_list.pop(0)

    for user_id in user_id_list:
        user_row = user_id.select('td')
        ranking = user_row[0].getText()
        user_id_string = user_row[1].getText()
        print(ranking +" : "+ user_id_string)
        one_user_solving_list = user_solving_number.crawling_user_num(user_id_string)
        one_result = {}
        one_result['user_id'] = user_id_string
        one_result['rank'] = int(ranking)
        one_result['solving_problem'] = one_user_solving_list
        json_one = json.dumps(one_result)
        result.append(json_one)
    

with open("ranker_data.json", "w") as outfile:
    json.dump(result, outfile)



