import os
import random
import string
import datetime
from threading import Thread
from multiprocessing import Process


def file_generator(directory, number_of_files, size):
    os.makedirs(directory, exist_ok=True)
    for i in range(number_of_files):
        with open(f'{directory}/file_{i}.txt', 'w') as file:
            file.write(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size))))
    return f'-> {number_of_files} files were created in the {directory} directory'


def letter_counter_in_one_thread(directory, letter_to_find):
    count_letters = 0
    files = os.listdir(directory)
    for file in files:
        with open(f'{directory}/{file}') as f:
            count_letters += f.read().count(letter_to_find)

    return f'Letter "{letter_to_find}" was found {count_letters} times'


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    files = os.listdir(directory)
    groups = [files[i::number_of_threads] for i in range(number_of_threads)]

    def letter_count(group):
        count = 0
        for file in group:
            with open(f'{directory}/{file}') as f:
                count += f.read().count(letter_to_find)
        return count

    for i in range(number_of_threads):
        thread = Thread(target=letter_count, args=(groups[i],))
        thread.start()

    return f'Letter "{letter_to_find}" was found {sum([letter_count(group) for group in groups])} times'


if __name__ == '__main__':
    print(file_generator('files', 12, 50))
    print('--------------------------------------------------------------------------')
    time_now1 = datetime.datetime.now()
    print(f"First func -> {letter_counter_in_one_thread('files', 'A')} - was done for time: {datetime.datetime.now() - time_now1}")
    print('--------------------------------------------------------------------------')

    time_now2 = datetime.datetime.now()
    thread2 = Thread(target=letter_counter_in_n_threads, args=('files', 'A', 4))
    thread2.start()
    thread2.join(timeout=0.2)
    print(f"Second func -> {letter_counter_in_n_threads('files', 'A', 4)} - was done for time: {datetime.datetime.now() - time_now2}")
    print('--------------------------------------------------------------------------')




















