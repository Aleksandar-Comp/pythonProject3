import os
import time
directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: '
              f'{formatted_time}, Родительская директория: {parent_dir}')
