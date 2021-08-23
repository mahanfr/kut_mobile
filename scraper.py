import requests
import jdatetime
from bs4 import BeautifulSoup
from unidecode import unidecode
import time
import json

data = {}
page_list = []

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
}

for i in range(1,3):
    time.sleep(10)
    url = f"https://kut.ac.ir/announcements?page={i}"
    request = requests.get(url,headers=header,verify=False)

    page_data = {}
    items_list=[]

    soup = BeautifulSoup(request.text,'lxml')
    divs = soup.find_all('div',class_="col-xs-6 col-sm-4 col-md-6")
    for div in divs:
        item_data = {}
        date_list = unidecode(div.span.text).split('/')
        if(int(date_list[0]) > 50):
            date_list[0] = f'13{date_list[0]}'
        else:
            date_list[0] = f'14{date_list[0]}'
        date = jdatetime.date(int(date_list[0]),int(date_list[1]),int(date_list[2])).togregorian()
        title = div.h3.text
        img = div.img['src']
        link = div.a['href']
        item_data['date'] = str(date)
        item_data['title'] = title
        item_data['img'] = img
        item_data['link'] = link
        items_list.append(item_data)

    page_data['page'] = i
    page_data['data-list'] = items_list
    page_list.append(page_data)

data['list'] = page_list
with open("sample.json", "w") as outfile:
    json.dump(data, outfile,indent=4)