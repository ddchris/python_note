import datetime as dt

print(dt.datetime.now())
print(dt.datetime.utcnow())

# 時間加減計算
tomorrow = dt.datetime.now() + dt.timedelta(days=1)

print(tomorrow)

# 時間取代(取得特定時間)
tomorrow = dt.datetime.replace(tomorrow, hour=0, minute=0, second=0)

print(tomorrow)


# 時間格式化
expires = dt.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")

print(expires)
