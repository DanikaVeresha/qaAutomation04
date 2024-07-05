"""
Write a timer function that will accept a web element and perform a tsk after 5 seconds
"""
from time import sleep
from typing import Callable


def timer(func: Callable, sec: int) -> None:
    sleep(sec)
    func()




