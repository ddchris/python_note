# -*- coding: utf-8 -*-

import os
import sys
from pprint import pprint
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

#______________抓取焦點新聞網址_____________

root_url = r'https://nba.udn.com/nba/index?gr=www'
root_html = requests.get(root_url)
root_html_text = root_html.text.encode('cp950', 'ignore').decode('cp950')
# 重新編碼解碼過濾編碼有問題字元

root_sp_obj = BeautifulSoup(root_html_text, 'html.parser')
# 利用 'html.parser' 方法解析原始碼, 建立 soup 物件

news_links_block = root_sp_obj.select('#news_body')
# 利用 soup 選擇器標定 id = 'news_body' 內所有 <a>

news_url_tags = news_links_block[0].find_all('a')
news_img_tags = news_links_block[0].find_all('img')

# 分別搜尋 id = 'news_body' 內所有 <a></a>,<img>

news_urls = []
img_urls = []
# 建立串列儲存焦點'新聞網址' & '圖片網址'

for url_tag in news_url_tags:
    news_urls.append( 'https://nba.udn.com/'+ url_tag.get('href'))

pprint(news_urls)
print()

for img_tag in news_img_tags:
    img_urls.append(img_tag.get('src'))

pprint(img_urls)
print()

#_____________繼續分析抓取到的每個焦點新聞網址_____________

headlines = []
contents = []
#建立串列儲存'新聞標題'與'新聞內容'

public_times = []
repoters = []
#建立串列儲存'發布時間'與'記者資訊'

for news_url in news_urls:
    news_html = requests.get(news_url)
    news_html_text = news_html.text.encode('cp950', 'ignore').decode('cp950')
    news_sp_obj = BeautifulSoup(news_html_text, 'html.parser')
    
    main_block = news_sp_obj.select('#story_body_content')
    headlines.append(main_block[0].find('h1').text)
    # 儲存新聞標題

    paragraph_tags = main_block[0].find('p')
    contents.append(paragraph_tags.text[0:-34])
    # 儲存新聞內容 (切字串去掉最後面粉絲團訊息)

    info_block = news_sp_obj.select('.shareBar__info--author')
    public_times.append(info_block[0].text[:16])
    repoters.append(info_block[0].text[16:])
    # 儲存發布時間與作者資訊 (切字串分開兩者)


pprint(headlines)
print()

for content in contents:
    print(content)
    print()


pprint(public_times)
print()
pprint(repoters)
print()