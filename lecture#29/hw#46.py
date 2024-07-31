import os
import random
import string
import datetime
import time
from threading import Thread


def file_generator(directory, number_of_files, size):
    """
    1. Write a function that generates `number_of_files` files in the `directory` directory.
    The contents of the files must be random and consist of large/small Latin letters, numbers and
    punctuation symbols.
    The file must contain a random number of characters ranging from `size/2` to `size` characters.
    def file_generator(directory, number_of_files, size)
    Be careful: file_generator('files', 200, 1000_000) ~150 Mb
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_files):
        with open(f'{directory}/file_{i}.txt', 'w') as file:
            file.write(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(size // 2, size))))

    return number_of_files


def letter_counter_in_one_thread(directory, letter_to_find):
    """
    2. Write a function (usual, that runs in single thread) that returns the number of letters
    `letter_to_find` in all files in the directory `directory`
    def letter_counter_in_one_thread(directory, letter_to_find)
    """
    count_letters = 0
    files = os.listdir(directory)
    for file in files:
        with open(f'{directory}/{file}') as f:
            count_letters += f.read().count(letter_to_find)

    time.sleep(0.5)
    print(f'Result "Thread" -> {count_letters} times')
    return count_letters


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    """
    3. Write a function that returns the number of letters `letter_to_find` in all files in the
    directory `directory`
    The function should split the files in the directory into `number_of_threads` groups, and
    read/count the letters for each group in a separate thread.
    Groups should be split equally as it is possible.
    def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
    """
    files = os.listdir(directory)
    groups = [files[i::number_of_threads] for i in range(number_of_threads)]
    counter = 0
    for group in groups:

        def letter_counter(group):
            nonlocal counter
            count_letters = 0
            for file in group:
                with open(f'{directory}/{file}') as f:
                    count_letters += f.read().count(letter_to_find)
            counter += count_letters

            time.sleep(0.1)
            print(f'Result "Threads" -> {count_letters} times')
            return count_letters

        thread = Thread(target=letter_counter, args=(group,))
        thread.start()
        thread.join(timeout=0.2)

    print(f'Total count result "Threads" -> {counter} times')
    return counter


def main():
    print(f"{file_generator('files', 12, 100)} files were created\n"
          f"------------------------------------------------")

    time1 = datetime.datetime.now()
    thread1 = Thread(target=letter_counter_in_one_thread, args=('files', 'A'))
    thread1.start()
    thread1.join()
    t1 = datetime.datetime.now() - time1
    print(f'Lead time "Thread" -> {t1}\n------------------------------------------------')

    time2 = datetime.datetime.now()
    letter_counter_in_n_threads('files', 'A', 4)
    t2 = datetime.datetime.now() - time2
    print(f'Lead time "Threads" -> {t2}\n------------------------------------------------')

    if t1 > t2:
        print(f'"Thread" lead time is {round((t2 / t1), 4)}..... times slower than "Threads" lead time\n'
              f'------------------------------------------------')
    else:
        print(f'"Threads" lead time is {round((t1 / t2), 4)}..... times faster than "Thread" lead time\n'
              f'------------------------------------------------')


if __name__ == '__main__':
    main()

