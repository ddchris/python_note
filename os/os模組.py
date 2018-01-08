import os

# 利用 open('檔名','操作方式與格式') 來打開或創建檔案
fout = open('oops.txt', 'wt')

# 利用 print() 將字串寫入檔案 
print('Oops, I create a file', file = fout)
fout.close()

# 利用 os.path.exist('檔名') 檢查檔案是否存在
os.path.exists('oops.txt')
os.path.exists('./oops.txt')
os.path.exists('waffles')
os.path.exists('.')
os.path.exists('..')
os.path.exists('~')

# 利用 os.path.isfile('檔名') 判斷檔案是否為一般檔案
os.path.isfile('oops.txt')

# 利用 os.path.isdir('檔名') 判斷檔案是否為資料夾目錄
os.path.isdir('oops.txt')
os.path.isdir('.')

# 利用 os.path.isbas('路徑字串') 判斷路徑是否為絕對路徑
os.path.isabs('/var/local')
os.path.isabs('../var/local')

# 利用 os.rename('原檔名','新檔名') 來更改名稱
os.rename('oops.txt','OOPS.txt')

# 利用 os.link('原檔名','新檔名') 來產生永久連結(hard-link)
# 利用 os.symlink('原檔名','新檔名') 產生符號連結(symbolic-link)
# 利用 os.islink('檔名') 來判斷檔案是否為符號連結
os.link('OOPS.txt', 'yikes.txt')
os.symlink('OOPS.txt', 'jeepers.txt')
os.path.exists('yikes.txt')
os.path.exists('jeepers.txt')

os.path.islink('yikes.txt')
os.path.islink('jeepers.txt')

# 利用 copy('原檔名','新檔名') 來複製檔案
import shutil
shutil.copy('OOPS.txt','D:/oooooooo.txt')

# 利用 abspath('檔名') 取得檔案絕對路徑
os.path.abspath('.')
os.path.abspath('../../oooooooo.txt')

# 利用 realpath('檔名') 取得捷徑檔的絕對路徑
os.path.realpath('.')
os.path.abspath('../../oooooooo.txt')

# 利用 remove('檔名') 刪除檔案
if os.path.exists('OOPS.txt'):
    os.remove('OOPS.txt')
os.path.exists('OOPS.txt')

# 利用 mkdir('檔名') 建立資料夾
# 利用 rmdir('檔名') 刪除'空'資料夾
# 利用 listdir('檔名') 刪除'空'資料夾
os.mkdir('poem')
os.path.exists('poem')
os.rmdir('poem')
os.path.exists('poem')

os.mkdir('poem')
os.listdir('poem')

os.mkdir('poem/test1')
file = open('./poem/test1/test.txt', 'wt')
file.close()
os.listdir('poem')






















