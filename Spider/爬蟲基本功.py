# -*- coding: utf-8 -*-
import re

# _______________步驟一 解析網址 _________________

# 網址解析工具 - urlparse
from urllib.parse import urlparse
from pprint import pprint

url = r'https://nba.udn.com/nba/index?gr=www'
o = urlparse(url)

print('scheme= {}'.format(o.scheme))
print('netloc= {}'.format(o.netloc))
print('path= {}'.format(o.path))
print('query= {}'.format(o.query))
print('port= {}'.format(o.port))

# 取得網頁原始碼 - requests 模組
import sys
import requests


url_1 = r'https://nba.udn.com/nba/index?gr=www'
html = requests.get(url_1)
html_decode = html.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
pprint(html_decode)
# .text 取得 response 物件的文字"字串"
#  使用 pprint 自動換行功能讓資料更清楚

if re.findall('焦點新聞',html_decode):
    print(re.findall('焦點新聞',html_decode))

註解 ='''順道一提，在下用 Python3 試寫這個網路爬蟲的時候有遇到唯一一個讓在下覺得挺難搞的問題，那就是中文的 windows「命令提示字元」(cmd) 編碼預設是：cp950 ，而 Python3 的預設程式碼編碼是：utf-8 (cp65001)，另外通常網頁的編碼也是 utf-8 (cp65001)，這時候就很有可能在執行 print() 指令時出現 「UnicodeEncodeError: 'cp950' codec can't encode character ... ...」的錯誤，進而導致程式腳本執行中斷。 '''

#_________ 步驟二. 使用 正規表示法 Regex "匹配網頁特定資料"___________


pat = re.compile('[a-z]+')
# 可先用 compile() 編譯欲匹配'模式',提升之後匹配速度


# match() 從頭逐字元檢查,一有不符合即中斷,回傳自開頭匹配之'字串 match物件' (盡可能地找最長)
m = pat.match('tem12po')
m1 = pat.match('1tempo23')
print(m)
# <_sre.SRE_Match object; span=(0, 3), match='tem'>

print(m1)
# None

# search() 回傳第一組匹配字串 'match物件'
m2 = pat.search('1temp1oppp23')
print(m2)
# <_sre.SRE_Match object; span=(1, 5), match='temp'>


# findall() 回傳指定字串中所有匹配字串之'串列'
m3 = pat.findall('1temp1oppp23')
print(m3)
# ['temp', 'oppp']


# 練習抓 e-mail

url_auth = r'https://auth.cht.com.tw/ldaps'
html_auth = requests.get(url_auth)
html_auth_text = html_auth.text.encode('cp950', 'ignore').decode('cp950')
 

regex = re.compile('[\w]+@[a-zA-Z0-9]+\.[a-zA-Z0-9\.]+')
email = regex.findall(html_auth_text)
print(email)


#_________ 步驟三. 網頁解析 使用 BeautifulSoup ___________

from bs4 import BeautifulSoup

url_lott = r'http://www.taiwanlottery.com.tw/'

html_lott = requests.get(url_lott)
html_lott_text = html_lott.text.encode('cp950', 'ignore').decode('cp950')
sp_obj = BeautifulSoup(html_lott_text, 'html.parser')

print(sp_obj.find('title'))
# sp 物件之 find() 回傳 <class 'bs4.element.Tag'>
# <class 'bs4.element.Tag'> 可接著用 get() 獲得 html 屬性

pprint(sp_obj.select('.contents_box02 .ball_tx.ball_green'))
# sp 物件之 select() 回傳一串列包含許多 <class 'bs4.element.Tag'>




# 取得某元素屬性

#方法一
data = sp_obj.find('div', {'id':'more_right'})
print(data.get('class'))


#方法二
pattern = re.compile('class="[\w]+"')
string = str(sp_obj.select('#more_right'))
# 將 select 傳回之 list 轉成 string

pprint(pattern.search(string).group()) #用 regex search() 抓出 class
# class="font_glay10"    


#______________抓取樂透威力彩開獎號碼_______________

url_lott = r'http://www.taiwanlottery.com.tw/'

html_lott = requests.get(url_lott)
html_lott_text = html_lott.text.encode('cp950', 'ignore').decode('cp950')
sp_obj = BeautifulSoup(html_lott_text, 'html.parser')

el = sp_obj.select('#rightdown')

el2 = el[0].find('div',{'class': 'contents_box02'})
# 找出第一個 class = 'contents_box02' 的 div tag

el3 = el2.find_all('div', {'class': 'ball_tx'})


print('本期樂透號碼: ', end='')
for number in el3:
    print(number.text, end= '')

red = el2.find('div',{'class': 'ball_red'})
# 抓紅球號碼

print('第二區:', red.text, end='' )


print()
print()
print()
#______________抓取某網頁所有圖片並存在資料夾_____________

url_nba = r'https://nba.udn.com/nba/index?gr=www'
html_nba = requests.get(url_nba)
html_nba_text = html_nba.text.encode('cp950', 'ignore').decode('cp950')
sp_obj_nba = BeautifulSoup(html_nba_text, 'html.parser')

# 建立儲存目錄
import os
from urllib.request import urlopen

imgs_dir = 'imgs/' 
if not os.path.exists(imgs_dir):
    os.mkdir(imgs_dir)

# 取得所有 <a>, <img> 因圖片幾乎藏在這兩個標籤

all_links = sp_obj_nba.find_all(['a','img'])
for link in all_links:
    src = link.get('src')
    href = link.get('href')
    attrs = [src, href]
    for attr in attrs:
        if attr != None and ('.jpg' in attr or '.png' in attr):
            full_path = attr
            file_name = full_path.split('/')[-1]    # 取得圖檔名稱
            ext = file_name.split('.')[-1] # 取得副檔名
            file_name = file_name.split('.')[-2] # 取得主檔名

            print('主檔名: ',file_name)
            print('副檔名: ',ext)
            print('路徑: ',full_path)

            if 'jpg' in ext:
                file_name += '.jpg'
            else:
                file_name += '.png'

            try:
                image = urlopen(full_path)
                f = open(os.path.join(imgs_dir,file_name), 'wb')
                f.write(image.read())
                f.close()
            except:
                print('無法讀取')