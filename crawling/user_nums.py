import requests
from bs4 import BeautifulSoup

user_id = "mor2222"  # mock user id

res = requests.get('https://www.acmicpc.net/user/'+user_id)
soup = BeautifulSoup(res.content, 'html.parser')

problem_numbers = soup.select('.problem_number')

user_num = []

for num in problem_numbers:
    user_num.append(num.getText())


