#!/user/bin/env python3
#coding:utf-8
import time,threading

balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		#先获取锁
		lock.acquire()
		try:
			change_it(n)
		finally:
			#然后释放锁，以免后续线程无法调用该函数
			lock.release()

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)