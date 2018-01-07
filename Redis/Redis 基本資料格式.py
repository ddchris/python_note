
import redis

# 建立一個連結到 redis 伺服器的 Redis 物件
conn = redis.Redis('localhost',6379)

# ______字串________

# 列出所有鍵
conn.keys('*')

# 利用 set(變數名稱,變數值)　設定一個變數
conn.set('str','hello!')
conn.set('str2','world')
conn.set('int',25)
conn.set('float',25.432)

# 利用 get(變數名稱)　取得一個變數值（位元格式）
conn.get('str')
conn.get('str2')
conn.get('float')
#b'25.432'

# 利用 setnx(變數名稱,變數值)　設定變數,可防止覆寫
conn.setnx('str','hello!')

# 利用 getset(變數名稱,新值)　取得舊值,並同時設為新值
conn.getset('str','Ooops!')
conn.get('str')

# 利用 getrange(變數名稱,start,end)　取得子字串
# 利用 setrange(變數名稱,starｔ)　替換子字串
conn.getrange('str',-4,-1)
conn.setrange('str', 1, 'ice')
conn.get('str')

# 利用　mset({鍵1:值1, 鍵2:值2 ...}) 一次設定多個鍵
# 利用　gset{鍵1,鍵2) 一次取得多個值
conn.mset({'pie':'cheery', 'cordial':'sherry'})
conn.mget('pie', 'cordial')

#　利用 delete() 來刪除鍵
conn.delete('pie')


# ______串列________


#　利用 lpush(串列名稱,值1,值2...) 來建立串列,不存在建立,資料皆從 "前方" 加入!!
conn.lpush('zoo', 'alligator', 'duck', 'monkey')
conn.lpush('zoo', 'fish')
conn.lpush('fruits', 'lemon', 'watermelon', 'banana')

conn.lpush('numbers', 1, 2, 3)
conn.lpush('numbers', 4, 5, 6)

# 利用 ltrim(串列名稱, start,end) 來修剪串列
conn.ltrim('zoo',0,3)
conn.ltrim('fruits',0,2)
conn.ltrim('numbers',0,5)

# 利用 lrange(串列名稱,start,end) 取得串列. ps.輸入0,-1取得全部
conn.lrange('zoo',0,-1)
conn.lrange('fruits',0,-1)
conn.lrange('numbers',0,-1)
# [b'6', b'5', b'4', b'3', b'2', b'1']

# 利用 lset(串列名稱,位移值,插入值) ps.覆寫原有值!
conn.lset('numbers',0,7)
conn.lrange('numbers',0,-1)

# 利用 rpush(串列名稱,插入值) 在尾端插入
conn.rpush('zoo','turtose')
conn.lrange('zoo',0,-1)

# 利用 lindex(位移值) 取得某位置的值
conn.lindex('zoo',1)



# _______字典________

# 利用 hmset(字典名稱,{鍵1:值1,鍵2:值2...}) 設定字典
# 利用 hmget(字典名稱,鍵1,鍵2...}) 取得多個欄位值串列
conn.hmset('song',{'do':'a deer','re':'about dog'}) 
conn.hmget('song','do','re') 

# 利用 hkeys (字典名稱) 取得字典所有鍵的串列
# 利用 hvals (字典名稱) 取得字典所有值的串列
# 利用 hgetall (字典名稱) 取得整個字典
conn.hkeys('song')
conn.hvals('song')
conn.hgetall('song')

# 利用 hset(字典名稱,鍵,值) 設定單一鍵值對
# 利用 hsetnx(字典名稱,鍵,值) 設定單一鍵值對(防止覆寫)
# 利用 hget(字典名稱,鍵) 取得單一值
conn.hset('song','aaa','ccc')
conn.hsetnx('song','bbb','ddd')
conn.hget('song','aaa')

# 利用 hlen(字典名稱) 取得字典長度
conn.hlen('song')

# 利用 hlen(字典名稱) 取得字典長度



