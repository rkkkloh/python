# daemon thread = a thread that runs in the background, not important to programto run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    #print()
    #print()
    count = 0
    while True:
        time.sleep(1)
        count+=1
        print('logged in for:',count,'seconds')


x = threading.Thread(target=timer,args=(),daemon=True)
# x.setDaemon(True) # call this before starting the thread we wish to set as a daemon thread (Ture/False)
x.start()

print(x.isDaemon())
answer = input("Enter your name\n")


