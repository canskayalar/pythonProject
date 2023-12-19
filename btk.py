from threading import Thread
from time import sleep

class cansu(Thread):
    def run(self):
        for i in range(10):
            print('cansu')
            sleep(0.3)

class kayalar(Thread):
    def run(self):
        for i in range(10):
            print('kayalar')
            sleep(0.3)


k1 = cansu()
k2= kayalar()

k1.start()
k2.start()

k1.join()
k2.join()

print("işlem tamamlandı")
