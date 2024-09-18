from multiprocessing import Pool, cpu_count
import time
import argparse

def init_worker(minutes):
    global stress_minutes
    stress_minutes = minutes

def f(x):
    timeout = time.time() + 60 * stress_minutes  # X minutes from now
    while True:
        if time.time() > timeout:
            break
        x * x

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Utilizes all available CPU cores for a specified number of minutes to generate load.")
    parser.add_argument("stress_mins", type=float, help="Duration in minutes to stress the CPU.")
    args = parser.parse_args()
    
    processes = cpu_count()
    print('Utilizing %d cores\n' % processes)
    
    pool = Pool(processes, initializer=init_worker, initargs=(args.stress_mins,))
    pool.map(f, range(processes))