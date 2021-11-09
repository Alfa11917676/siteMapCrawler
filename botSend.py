import crawler
import requests
import getEnv


dataReceived = crawler.runCrawler()
api_id = getEnv.BOTID
chat_id = getEnv.CHATID
print (api_id)
if dataReceived== 'No new links':
      base_url = f'https://api.telegram.org/bot{api_id}/sendMessage?chat_id={chat_id}&text={dataReceived}'
      base_url1 = f'https://api.telegram.org/bot2138883003:AAGDXKLhaugdUNbkH1b9lj2CMiTQQiIR_S4/sendMessage?chat_id=-728115572&text={dataReceived}'
      response = requests.get(base_url)
      response1 = requests.get(base_url1)
      print(response.json())
      print(response1.json())

else:

           for i in range(len(dataReceived)):
            base_url = f'https://api.telegram.org/bot{api_id}/sendMessage?chat_id={chat_id}&text={dataReceived[i]}'
            base_url1 = f'https://api.telegram.org/bot2138883003:AAGDXKLhaugdUNbkH1b9lj2CMiTQQiIR_S4/sendMessage?chat_id=-728115572&text={dataReceived[i]}'
            response = requests.get(base_url)
            response1 = requests.get(base_url1)
            print (response.json())
            print (response1.json())

print (base_url)
print (base_url1)


#https://api.telegram.org/bot2057246573:AAE6glg4oRgzn1kohhf-XzkA5JsCZFuW7k4/getUpdate
