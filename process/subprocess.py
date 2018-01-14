# _*_ coding:utf-8 _*_
  
import os

# 取得目前解譯器程序 ID
os.getpid()
# 取得目前解譯器工作目錄
os.getcwd()
# 取得 user ID (Unix available)
os.getuid()
# 取得 group ID (Unix available)
os.getgid()


# _______ 使用 subprocess 建立一個程序 ________

import subprocess

# 用 getoutput('shell cml') 在 shell 中執行程式並取得標準輸出
result = subprocess.getoutput('date') 
'Sun Jan 14 19:37:10 CST 2018'
result = subprocess.getoutput('date -u')
'Sun Jan 14 12:15:22 UTC 2018'
result = subprocess.getoutput('date -u| wc')
'      1       6      29'

# check_output([cmd, attrs]) 指令與引數以串列方式傳入
result = subprocess.check_output(['date','-u'])
b'Sun Jan 14 12:51:30 UTC 2018\n'

# 用 getstatusoutput() 取得  (程序退出狀態,輸出) tuple
result = subprocess.getstatusoutput('date')
(0, 'Sun Jan 14 20:54:57 CST 2018')

# 只想取得程序退出狀態用 call([cmd, attrs])
result = subprocess.call(['date','-u'])
0 (表示成功退出)