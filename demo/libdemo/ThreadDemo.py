# Create a new thread to print numbers from 1 to 10 02 03
#
from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(f"Child -> {i}")


t1 = PrintThread()
t1.start()

for i in range(1, 11):
    print(f'Main -> {i}')
