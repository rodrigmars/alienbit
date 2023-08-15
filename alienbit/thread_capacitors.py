import time
from threading import Thread, current_thread
from collections import deque
from random import randrange, choice
from fifo import fifo_deque
from core import get_estrategy, hard_verse

def thread_capacitor() -> None:

    fifo_message, fifo_score, consumer_message, consumer_score = fifo_deque()

    def producer_flux(fifo_message:deque, fifo_score:deque, total_time:int, strategy:dict):

        fifo_message.appendleft((current_thread().name, 'Starting'))

        time.sleep(total_time)

        score = hard_verse(strategy["economy"])(strategy["coin"])(strategy["economy_"])(strategy["percent"])

        fifo_score.appendleft((current_thread().name, f'score:{score}'))

        time.sleep(.1)

        fifo_message.appendleft((current_thread().name, 'Exiting'))

    TOTAL_CAPACITORS:int = 2

    thread_message = Thread(target=consumer_message, 
                            args=(fifo_message, TOTAL_CAPACITORS), 
                            name="thread_monitor")
    thread_message.start()
    
    Thread(target=consumer_score, 
           args=(fifo_message, fifo_score, TOTAL_CAPACITORS), 
           name="thread_monitor").start()

    for i in range(TOTAL_CAPACITORS):

        Thread(target=producer_flux, 
               args=(fifo_message, fifo_score, randrange(1, 9), get_estrategy()), 
               name=f"flux_{i}").start()

    thread_message.join()