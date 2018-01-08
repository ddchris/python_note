""" 解壓縮.zip檔案 """
import zipfile

# 讀取檔案使之成為程式物件
files = zipfile.ZipFile('calculator_plus.zip')

# 顯示壓縮黨內包含哪些檔案
files.namelist()

# 解壓縮單一檔案 ->  .extract(r'檔案名稱',r'檔案位置')
files.extract(r'calculator_plus/image/AC.png', r'C:\Users\chris2012\Documents\visual studio 2017\Projects\Python 標準函式庫應用\Python 壓縮與解壓縮')

# 解壓縮所有檔案 ->  .extract(r'檔案位置')
files.extractall
(r'C:\Users\chris2012\Documents\visual studio 2017\Projects\Python 標準函式庫應用\Python 壓縮與解壓縮')

#呼叫close(),結束執行步驟
files.close()


""" 壓縮成.zip檔案 """

# 格式 ->  zipfile.ZipFile(r'存放路徑\壓縮檔檔案名稱()', mode='w') 
# 其中'w'為寫入模式, 此步驟會產生一個壓縮檔!
zip_file = zipfile.ZipFile(r'C:\zipfile\picture',mode='w')

# 格式 ->  zipfile.write(r'欲壓原檔案位置','解壓後看到的名稱')
# 此步驟會將特定檔案寫入產生的zip中
zip_file.write(r'C:\zipfile\AC.png','ppiicc')

