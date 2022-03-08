from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = 'https://kndl.kr/kndl/requests'
data = {
    'id':'kndl',
    'pw':'kndl',
    'login_maintain':0
}

session = requests.session()
response = session.post(url, data=data)

response.raise_for_status()

bsObject = BeautifulSoup(response.text, 'html.parser')

for link in bsObject.find_all('a'):
    print(link.test.strip(), link.get('href'))