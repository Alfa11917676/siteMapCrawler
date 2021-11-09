import requests
from bs4 import BeautifulSoup
import os
import time

def runCrawler():
    url = 'https://www.coingecko.com/sitemap'

    headers = {"Accept": "application/xml"}
    datas=[]
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    unfilteredDetails = soup.find('loc')
    filteredDetails = requests.get(unfilteredDetails.text)
    filteredDetails = filteredDetails.text
    filteredDetails = BeautifulSoup(filteredDetails,'html.parser')
    d = filteredDetails.find_all("xhtml:link")
    if os.path.exists('./reference.txt'):
        for details in d:
            href = details.get('href')
            datas.append(href)

    else:
        for details in d:
            href = details.get('href')
            with open('reference.txt','a') as f:
                f.writelines( href+'\n')
            f.close()
    try:

        file2 = open("reference.txt")

        txt2 = file2.read().strip().splitlines()


        file2.close()

        sites = set()
        for j in txt2:
            sites.add(j)

        res = list()
        count = 0
        for i in datas:
            count += 1
            if i not in sites:
                sites.add(i)
                res.append(i)

        file = open("reference.txt", "a")
        for j in datas:
            file.write(j + "\n")
        file.close()
        if res:
            return res
        else:
            return "No new links"
    except Exception as e:
        return e

if __name__ == '__main__':
    print (runCrawler())