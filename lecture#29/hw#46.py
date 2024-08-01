import os
import random
import string
import datetime
import threading
from threading import Thread


def file_generator(directory, number_of_files, size):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_files):
        with open(os.path.join(directory, f'file_{i}.txt'), 'w') as file:
            file.write(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size))))

        # with open(f'{directory}/file_{i}.txt', 'w') as file:
        #     file.write(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size))))

    return number_of_files


def letter_counter_in_one_thread(directory, letter_to_find):
    count_letters = 0
    files = os.listdir(directory)
    for file in files:
        with open(os.path.join(directory, file)) as f:
            count_letters += f.read().count(letter_to_find)

        # with open(f'{directory}/{file}') as f:
        #     count_letters += f.read().count(letter_to_find)

    return count_letters


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    files = os.listdir(directory)
    groups = [files[i::number_of_threads] for i in range(number_of_threads)]
    results = []
    lock = threading.Lock() # Создаю объект блокировки

    def count_letters(groups): # Функция для подсчета букв
        count = 0
        for file in group:
            with open(os.path.join(directory, file)) as f:
                count += f.read().count(letter_to_find)

            # with open(f'{directory}/{file}') as f:
            #     count += f.read().count(letter_to_find)
        with lock: # Блокирую доступ к общему ресурсу
            results.append(count)

    # Создаю потоки
    threads = []
    for group in groups:
        thread = Thread(target=count_letters, args=(group,))
        thread.start()
        threads.append(thread)

    # Жду завершения всех потоков
    for thread in threads:
        thread.join()

    return results


def client_code(directory, number_of_files, size, letter_to_find, number_of_threads):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_files):
        with open(os.path.join(directory, f'file_{i}.txt'), 'w') as file:
            file.write(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size))))

        # with open(f'{directory}/file_{i}.txt', 'w') as file:
        #     file.write(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size))))

    counter = 0
    files = os.listdir(directory)
    start3 = datetime.datetime.now()
    for file in files:
        with open(os.path.join(directory, file)) as f:
            counter += f.read().count(letter_to_find)

        # with open(f'{directory}/{file}') as f:
        #     counter += f.read().count(letter_to_find)
    time3 = datetime.datetime.now() - start3

    groups = [files[i::number_of_threads] for i in range(number_of_threads)]
    results_threads = []
    lock = threading.Lock()

    def count_letters(groups):
        count = 0
        for file in group:
            with open(os.path.join(directory, file)) as f:
                count += f.read().count(letter_to_find)

            # with open(f'{directory}/{file}') as f:
            #     count += f.read().count(letter_to_find)
        with lock:
            results_threads.append(count)

    threads = []
    start4 = datetime.datetime.now()
    for group in groups:
        thread = Thread(target=count_letters, args=(group,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    time4 = datetime.datetime.now() - start4

    total_count_letters = sum(results_threads)

    if time3 > time4:
        print(f'-> The "Threads" method is faster on {time3 - time4}')
    else:
        print(f'-> The "Thread" method is faster on {time4 - time3}')

    return f'{number_of_files} | {counter} -> {time3} | {total_count_letters} -> {time4} |'


if __name__ == '__main__':
    print(f'-> Number of files created: '
          f'{file_generator("files", 12, 50)}\n')

    start1 = datetime.datetime.now()
    print(f'-> Result "Thread": '
          f'{letter_counter_in_one_thread("files", "A")} times')
    print(f'-> Lead time "Thread": {datetime.datetime.now() - start1}\n')

    start2 = datetime.datetime.now()
    print(f'-> Result "Threads": '
          f'{letter_counter_in_n_threads("files", "A", 6)} times')
    print(f'-> Lead time "Threads": {datetime.datetime.now() - start2}\n')

    print(f'-> Result Client Code: \n'
          f'\tNumber of files | Number of letters -> Time "Thread" | Number of letters -> Time "Threads" | \n'
          f'\t{client_code("files", 12, 50, "A", 4)}')




