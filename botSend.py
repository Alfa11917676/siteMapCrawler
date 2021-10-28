import crawler
import requests
import getEnv


dataReceived = crawler.runCrawler()
api_id = getEnv.BOTID
chat_id = getEnv.CHATID
print (api_id)

base_url = f'https://api.telegram.org/bot{api_id}/sendMessage?chat_id={chat_id}&text={dataReceived}'
print (base_url)
response = requests.get(base_url)
print (response)

