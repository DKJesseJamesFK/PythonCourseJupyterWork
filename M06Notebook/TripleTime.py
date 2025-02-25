import multiprocessing
import random
import time

def print_time():
    fmt = "The current time is %I:%M:%S%p."
    time.sleep(random.uniform(0, 1))
    current_time = time.gmtime()
    print(time.strftime(fmt, current_time))

if __name__ == "__main__":
    for i in range(3):
        p = multiprocessing.Process(target=print_time)
        p.start()