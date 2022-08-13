from threading import*
import time
def f1(n):
    for x in range(n):
        time.sleep(4)
        print(current_thread().name,x)
start=time.time()
def f2():
    for x in range(6,10):
        time.sleep(3)
        print(current_thread().name,x)
end=time.time()
def f3():
     while True:
         print(current_thread().name,'hello')
t1=Thread(target=f1,args=[5],name='thread1')     #creating a thread of f1
t1.start()
t1.join()       #join() blocks the another process until the called function terminates
t2=Thread(target=f2,name='thread2')              #creating a thread of f2
t2.start()
t2.join()
t3=Thread(target=f3,name='thread3',daemon=True)
t3.start()
print(current_thread().name)
print("time taken:",end-start)
