# -*- coding: utf-8 -*-

'''
Threading:
在一個角本中,使 python 同一時間內運行多個線程, 有效節省運算時間
'''
'''
多線程本身沒有 return 值, 所以一定要把運算出的結果放入 Queue 中. 
等所有線程結束後再自主線程取出接著運算,對於資源,加鎖是個重要的環節。
因為 python 原生的 list,dict 等，都是 not thread safe 的。而 Queue，
是 thread safe 的，因此在滿足使用條件下，建議使用儲列。
'''
from queue import Queue

import time
import threading as thd
# active_count() 查看目前有多少個活的線程(不包含已結束線程)
# enumerate() 返回目前所有線程資料 list (不包含已結束線程)
# current_thread() 返回當前運行的線程

def job1(l,q,i):
    print('Thread' + str(i+1) + ' start!')
    for j in range(len(l)):
        l[j] = l[j]**2
        time.sleep(0.1)
    '將計算結果逐次放入 queue 中'
    q.put(l)
    print('Thread' + str(i+1) + ' finish!')

def job2(l,q,i):
    print('Thread' + str(i+1) + ' start!')
    for j in range(len(l)):
        l[j] = l[j]**3
        time.sleep(0.1)
    '將計算結果逐次放入 queue 中'
    q.put(l)
    print('Thread' + str(i+1) + ' finish!')

def job3(l,q,i):
    print('Thread' + str(i+1) + ' start!')
    for j in range(len(l)):
        l[j] = l[j]**4
        time.sleep(0.1)
    '將計算結果逐次放入 queue 中'
    q.put(l)
    print('Thread' + str(i+1) + ' finish!')

def job4(l,q,i):
    print('Thread' + str(i+1) + ' start!')
    for j in range(len(l)):
        l[j] = l[j]**5
        time.sleep(0.1)
    '將計算結果逐次放入 queue 中'
    q.put(l)
    print('Thread' + str(i+1) + ' finish!')

jobs = [job1,job2,job3,job4]

data = [[1,2,3,567,454,5656,5634323423434234234],[3,4,5,56],[6,7,3],[6,5,5,67,435324,2324]]

def multithreading(data):
    q = Queue()
    threads = []
    for i in range(4):
        '注意 target 處 job 只是索引, 所有引數要從後方 args 以 tuple 傳入'
        t = thd.Thread(target=jobs[i], args=(data[i], q, i) )
        t.start()

        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for _ in range(4):
        '每次從 Queue 拿出一個值'
        result.append(q.get())
    print('結果為: ', result)

multithreading(data)

"""
def T1_job():
    # print('This is an added Thread, number is {}'.format(thd.current_thread() ))
    print('T1 start')
    for i in range(10):
        print(i)
        time.sleep(0.1)
    print('In T1 目前線程為: ',thd.current_thread())
    print('T1 finish')

def T2_job():
    print('T2 start')
    print('In T2 目前線程為: ',thd.current_thread())
    print('T2 finish')

def main():
    '添加一個新線程, 並以 name 引數命名'
    add_T1_thread = thd.Thread(target= T1_job, name= 'T1')
    add_T1_thread.start()

    add_T2_thread = thd.Thread(target=T2_job, name='T2')
    add_T2_thread.start()

    print('目前有幾個線程: ', thd.active_count())
    print('目前線程列表: ', thd.enumerate())
    print('In main 目前線程為: ',thd.current_thread())

    '以 join() 把某線程綁至主線程, 等其結束才繼續執行主線程程序'
    add_T1_thread.join()
    #add_T2_thread.join()
    print('all down')

if __name__ == '__main__':
    main()
"""

