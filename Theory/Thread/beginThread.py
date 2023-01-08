from threading import Thread

shared_number = 0

def work(n):
    global shared_number
    print(f"number : {n}")

    for i in range(n):
        shared_number += 1

t1 = Thread(target=work, args=(5000000,))
t2 = Thread(target=work, args=(5000000,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"shared_number : {shared_number}")

