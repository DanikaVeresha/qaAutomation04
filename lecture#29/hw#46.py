import os
import random
import string
import datetime
from threading import Thread


def file_generator(directory, number_of_files, size):
    os.makedirs(directory, exist_ok=True)
    for i in range(number_of_files):
        with open(f'{directory}/file_{i}.txt', 'w') as file:
            file.write(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size))))
    return number_of_files


def letter_counter_in_one_thread(directory, letter_to_find):
    count_letters = 0
    files = os.listdir(directory)
    for file in files:
        with open(f'{directory}/{file}') as f:
            count_letters += f.read().count(letter_to_find)

    return count_letters


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    count_letters = 0
    files = os.listdir(directory)
    groups = [files[i::number_of_threads] for i in range(number_of_threads)]
    while number_of_threads > 0:
        number_of_threads -= 1

        for item in groups[number_of_threads]:
            # print(f'{groups[number_of_threads]}')
            thread = Thread(target=lambda: open(f'{directory}/{item}').read().count(letter_to_find))
            thread.start()
            thread.join(timeout=0.3)

            with open(f'{directory}/{item}') as f:
                letters = f.read().count(letter_to_find)
                # print(f'|-> Letters: {letters} |-> File: {item}')
                count_letters += letters

    return count_letters


if __name__ == '__main__':
    print(f'New {file_generator("files", 12, 50)} files were created with random content')
    print('--------------------------------------------------------------------------')

    time_now1 = datetime.datetime.now()
    print(f"Result of First func -> {letter_counter_in_one_thread('files', 'A')} times\n"
          f"Lead time: {datetime.datetime.now() - time_now1}")
    print('--------------------------------------------------------------------------')

    time_now2 = datetime.datetime.now()
    thread2 = Thread(target=letter_counter_in_n_threads, args=('files', 'A', 4))
    thread2.start()
    thread2.join(timeout=0.5)
    print(f"Result of second func -> {letter_counter_in_n_threads('files', 'A', 4)} times\n"
          f"Lead time: {datetime.datetime.now() - time_now2}")
    print('--------------------------------------------------------------------------')





































