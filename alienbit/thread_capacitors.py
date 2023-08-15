import time
from threading import Thread, current_thread
from collections import deque
from fifo import fifo_deque
from core import hard_verse

def producer_flux(fifo_message:deque, fifo_score:deque, total_time:int):

    fifo_message.appendleft((current_thread().name, 'Starting'))

    time.sleep(total_time)

    score = hard_verse("sadsa")(25)([.1, 25])(2.5)

    fifo_score.appendleft((current_thread().name, f'score:{score}'))

    time.sleep(.1)

    fifo_message.appendleft((current_thread().name, 'Exiting'))

def thread_capacitor() -> None:

    capacitors:list = [[ producer_flux, 2, "flux_01"], 
                       [ producer_flux, 2, "flux_02"], 
                       [ producer_flux, 1, "flux_03"]]

    fifo_message, fifo_score, consumer_message, consumer_score = fifo_deque()


    thread_message = Thread(target=consumer_message, 
                            args=(fifo_message, len(capacitors)), 
                            name="thread_monitor")
    thread_message.start()
    
    Thread(target=consumer_score, 
           args=(fifo_message, fifo_score, len(capacitors)), 
           name="thread_monitor").start()
        
    for flux in capacitors:

        Thread(target=flux[0], 
               args=(fifo_message, fifo_score, flux[1]), 
               name=flux[2]).start()

    thread_message.join()