from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    for num in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {num}\n')
            sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


start_time1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
stop_time1 = datetime.now()
print(f'Time_elapsed_1: {stop_time1 - start_time1}')

start_time2 = datetime.now()
thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
stop_time2 = datetime.now()
print(f'Time_elapsed_2: {stop_time2 - start_time2}')