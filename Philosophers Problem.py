import threading
import time
import random

NUM_PHILOSOPHERS = 5


forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

def philosopher(phil_id):
    left = phil_id
    right = (phil_id + 1) % NUM_PHILOSOPHERS

    while True:
        print(f"Philosopher {phil_id} is thinking.")
        time.sleep(random.uniform(1, 3))

        print(f"Philosopher {phil_id} is hungry.")


        if phil_id == 0:
            forks[right].acquire()
            forks[left].acquire()
        else:
            forks[left].acquire()
            forks[right].acquire()

        print(f"Philosopher {phil_id} is eating.")
        time.sleep(random.uniform(1, 2))


        forks[left].release()
        forks[right].release()
        print(f"Philosopher {phil_id} finished eating.")


threads = []
for i in range(NUM_PHILOSOPHERS):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
