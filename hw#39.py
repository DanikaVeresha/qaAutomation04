"""Task 39."""

import time
from contextlib import contextmanager


class Timer:
    def __init__(self):
        """Initialize Timer object with elapsed_time = 0."""
        self.elapsed_time = 0

    def __enter__(self):
        """Start measuring time."""
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop measuring time and add it to elapsed_time."""
        self.elapsed_time += time.time() - self.start

    def reset(self):
        """Reset elapsed_time to 0."""
        self.elapsed_time = 0


@contextmanager
def timer():
    """Context manager for measuring time."""
    start = time.time()
    yield
    elapsed_time = time.time() - start
    print(f'Elapsed time: {elapsed_time}')


if __name__ == '__main__':
    """Test Timer class and timer context manager."""
    with Timer() as t:
        time.sleep(1)
    print(f'Elapsed time: {t.elapsed_time}')
    time.sleep(1)
    with t:
        time.sleep(1)
    print(f'Elapsed time: {t.elapsed_time}')

    with Timer() as t2:
        time.sleep(1)
    print(f'Elapsed time: {t2.elapsed_time}')
    time.sleep(1)
    t2.reset()
    with t2:
        time.sleep(1)
    print(f'Elapsed time: {t2.elapsed_time}')
