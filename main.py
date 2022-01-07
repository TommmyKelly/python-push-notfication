import requests
import random
from pushbullet import Pushbullet
from varibales import token

url = 'https://type.fit/api/quotes'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/96.0.4664.110 Safari/537.36'}

r = requests.get(url, headers=headers)

dic = r.json()

random_quote = random.choice(dic)
text = f"{random_quote['text']} \nAuthor: {random_quote['author']}"

pb = Pushbullet(token)
push = pb.push_note('Quote of the day', text)
