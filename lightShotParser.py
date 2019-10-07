import requests, time, shutil, itertools
from bs4 import BeautifulSoup as bs


headers = {
    'accept':'*/*',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

base_url = 'https://prnt.sc/'

file_path = 'D:\pyth\parser\LightShotParser-master\img'

symbols = list('abcdefghijklmnopqrstuvwxyz0123456789')


def parser(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        imgUrl = soup.find('img', attrs={'class':'no-click screenshot-image'})
        if imgUrl is not None and imgUrl['src'] != '//st.prntscr.com/2019/09/03/1652/img/0_173a7b_211be8ff.png':
            return imgUrl['src']
        return None
    else:
        return None


def downloadImage(imgUrl, imgIndex):
    r = requests.get(imgUrl, stream=True)
    if r.status_code == 200:
        with open(file_path +'\\'+ imgIndex + '.png', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def foo(l):
     yield from itertools.product(*([l] * 6)) 

for x in foo(symbols):
    url_index=''.join(x)
    tempStr = ''.join(url_index)
    imgUrl = parser(base_url + tempStr, headers)
    if imgUrl is not None:
        print(imgUrl)
        downloadImage(imgUrl,tempStr)
    