import requests
from bs4 import BeautifulSoup
url = 'https://www.coingecko.com/sitemap'

headers = {"Accept": "application/xml"}

response = requests.request("GET", url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
unfilteredDetails = soup.find('loc')
filteredDetails = requests.get(unfilteredDetails.text)
filteredDetails = filteredDetails.text
filteredDetails = BeautifulSoup(filteredDetails, 'html.parser')
d = filteredDetails.find_all("lastmod")
for details in d:
    href = details.get('')
print (d)