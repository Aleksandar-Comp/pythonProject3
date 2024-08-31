import random
from threading import Thread, Lock
from time import sleep

thr_lock = Lock()


class Bank():
    counter = 0

    def __init__(self):
        self.balance = 0.0
        self.lock = Lock()

    def deposit(self):
        while Bank.counter < 199:
            if Bank.counter % 2 == 0:
                with thr_lock:
                    Bank.counter += 1
                    random_deposit = random.randint(50, 500)
                    self.balance += random_deposit
                    print(f"Пополнение: {random_deposit}. Баланс: {self.balance}")
                    if self.balance >= 500 and self.lock.locked():
                        self.lock.release()
                sleep(0.001)


    def take(self):
        while Bank.counter <= 199:
            if Bank.counter % 2 == 1:
                with thr_lock:
                    Bank.counter += 1
                    random_take = random.randint(50, 500)
                    print(f"Запрос на {random_take}")
                    if self.balance >= random_take:
                        self.balance -= random_take
                        print(f'Снятие: {random_take}. Баланс: {self.balance}')
                    else:
                        print(f'Запрос отклонён, недостаточно средств')
                        if not self.lock.locked():
                            self.lock.acquire()
                sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')