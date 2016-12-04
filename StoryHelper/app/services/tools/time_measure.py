from time import time

def measure(func):
    def measure_time(*args):
        start_time = time()
        func()
        print("--- %s seconds ---" % (time() - start_time))    
    return measure_time
    