# _*_ coding:utf-8 _*_

import os

poem = '''There is a young lady named Bright
        Whose speed is far faster than light
        She started one day
        I a relative way,
        And return on a previous night.'''

# 使用 open('檔案名稱', '打開方式' ) 打開檔案
# 打開方式(1st字) r:讀檔 , w:寫入, x: 檔案存在時寫入,a:附加在後
#        (2nd字) t:表文字檔(預設), b: 二進位檔
         
file = open('poem.txt','wt', encoding = 'utf-8')
file.write(poem)
file.close()

with open('poem.txt','r') as f:   # f 為 onen() 回傳的檔案物件
    for line in f:  
        print(line,end='')

print() 

poem2 = '''There is a young lady named Bright
        Whose speed is far faster than light
        She started one day
        I a relative way,
        And return on a previous night.
        There is a young lady named Bright
        Whose speed is far faster than light
        She started one day
        I a relative way,
        And return on a previous night.'''

fout = open('poem.txt','wt')
size = len(poem2)

offset = 0
chunk = 20

while True:
    if offset > size:
        break

    # 字串很大時可以"分段寫入"
    fout.write(poem2[offset:offset+chunk])
    offset += chunk
fout.close()

# 使用.read(字數) 讀入特定字數的字元,若沒提供引數則全部輸出!
fout = open('poem.txt','r')
text = fout.read(100)
print(text)
fout.close()


print() #___________________分隔線___________________
poem = ''

fin = open('poem.txt','rt')
chunk = 20
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
print('poem2:\n' + poem ,sep='',end='')

fin.close()
print(len(poem))


print() #___________________分隔線___________________

#_________ 使用'迭代器'讀取文字最方便_________

poem3 = ' poem3: '
file_in = open('poem.txt','r')

for line in file_in:
    poem3 += line
file_in.close()

print(poem3)


print() #___________________分隔線___________________
poem4 = ' poem4: '
file_in = open('poem.txt','r')
lines = file_in.readlines()
print('lines =', lines)  # readlines回傳一個'list', 每行為一元素,包含結尾換行符號'\n'

print() #___________________分隔線___________________
file_in.close()

print(poem4)
for line in lines:
    print(line,end='')


print() #___________________分隔線___________________
print() #___________________分隔線___________________

# 用 write 來寫入二進位檔案

bdata = bytes(range(0,255))
print('length of bdata = ', len(bdata))

file_out = open('b_file.txt','wb')
file_out.write(bdata)
file_out.close()

file_out = open('b_file.txt','rb')
bdata_lines = file_out.readlines()

for line in bdata_lines:
    print(line,end='')

print() #___________________分隔線___________________
print() #___________________分隔線___________________

# 分段寫入二進位檔案

file_out2 = open('b_file2.txt','wb')
size = len(bdata)
offset = 0
chunk = 30

while True:
    if offset < size:
        file_out2.write(bdata[offset:offset+chunk])
        offset += chunk
    else:
        break

# 讀取二進位檔案

file_out2 = open('b_file2.txt','rb')
bytes = file_out2.read()
print('逐次寫入資料: ',end='')
print(bytes)

print() #___________________分隔線___________________
print() #___________________分隔線___________________

# 使用 tell(),回傳從檔案一開始算起游標位置

file_out2 = open('b_file2.txt','rb')
print(file_out2.tell())
bytes = file_out2.read(10)
print(file_out2.tell())

# 使用 seek( offset, origin ) 改變游標位置
# origin = 0 由檔案開頭算起(offset > 0), =1 由目前位置算起(offset可為正或負), 
# =2 由檔案結尾算起(offset < 0)
 
file_out2.seek(30)
print(file_out2.tell())
bytes2 = file_out2.read(10)
print(file_out2.tell())
file_out2.seek(-10,2)
print(file_out2.tell())


print('bytes2= ',bytes2)


menu = \
{
    'breakfast':{
        'hours':'7-11',
        'items':{
            'breakfast burritos': '$6.00' ,'pancakes': '$4.00'
        }
    },
    'lunch': {
        'hours':'11-3',
        'items':{
                'hamburger': '$5.00'
            }
            
    },
    'dinner':{
        'hours': '3-10',
        'items':{
            'spaghetti': '$8.00'    
        }
    }
}





