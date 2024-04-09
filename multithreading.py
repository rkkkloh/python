# thread = a flow of execution. Like a seperate order of instructions.
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control of the Python interpreter

# cpu bound = program/task spends most of it's time wating for internal events(CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input,web scraping)
#            use multithreading
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You have done your breakfast")

def take_shower():
    time.sleep(5)
    print("You smells good")

def brush_teeth():
    time.sleep(4)
    print("Your teeth is crystal clean")

x = threading.Thread(target = eat_breakfast,args=())
x.start()
y = threading.Thread(target = take_shower,args=())
y.start()
z = threading.Thread(target = brush_teeth,args=())
z.start()

#x.join()
#y.join()
z.join()

#eat_breakfast()
#take_shower()
#brush_teeth()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())