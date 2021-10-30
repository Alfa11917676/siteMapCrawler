import requests
from bs4 import BeautifulSoup
import os
import time
def runCrawler():
    url = 'https://www.coingecko.com/sitemap'

    headers = {"Accept": "application/xml"}

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
            with open('freshRun.txt', 'ab') as f:
                f.write( href.encode('utf-8')+'\n'.encode('utf-8') )
            f.close()
    else:
        for details in d:
            href = details.get('href')
            with open('reference.txt','ab') as f:
                f.write( href.encode('utf-8')+'\n'.encode('utf-8') )
            f.close()
    try:
        with open('./reference.txt','rb') as d:
            read_first_line = d.readline()
            for last_read in d:
                pass
        refLastLine = last_read
        with open('./freshRun.txt','rb') as f:
            first_Line = f.readline()
            for last_line in f:
                pass
        freshLastLine =  (last_line)
        if refLastLine != freshLastLine:
            with open("freshRun.txt","rb") as f:
                with open("reference.txt", "wb") as f1:
                    for line in f:
                        f1.write(line)
            return (str(freshLastLine)[2:-1])
        else:
            return ('No new links added')
    except Exception as e:
        return e

if __name__ == '__main__':
    print (runCrawler())
