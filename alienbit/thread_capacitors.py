import time
from threading import Thread, current_thread
from collections import deque
from random import randrange, choice
from fifo import fifo_deque
from core import get_estrategy, hard_verse

def thread_capacitor() -> None:
    
    fifo_status_percent, \
        fifo_message, \
            fifo_score, \
                fifo_error, \
                    consumer_spinner, \
                        consumer_message, \
                            consumer_score, \
                                consumer_error = fifo_deque()


    def producer_flux(fifo_message:deque, fifo_score:deque, fifo_counter_processed:deque, total_time:int, strategy:dict):

        status_error = False

        try:

            raise Exception("Error teste")

            fifo_message.appendleft((current_thread().name, 'Starting'))

            time.sleep(total_time)

            score = hard_verse(strategy["economy"])(strategy["coin"])(strategy["economy_"])(strategy["percent"])

            fifo_score.appendleft((current_thread().name, f'score:{score}'))

            time.sleep(.1)

        except Exception as e:
            fifo_error.appendleft((current_thread().name, 'Error', e))
            status_error = True
        finally:
            fifo_message.appendleft((current_thread().name, 'Processed' if status_error is False else 'Processed with Error'))
            fifo_counter_processed.appendleft(1)
            print("finally chegando aqui ")

    TOTAL_CAPACITORS:int = 10

    thread_spinner = Thread(target=consumer_spinner, 
                            args=(fifo_status_percent,), 
                            name="thread_spinner")

    thread_spinner.start()

    thread_message = Thread(target=consumer_message, 
                            args=(fifo_status_percent, fifo_message, TOTAL_CAPACITORS), 
                            name="thread_message")
    thread_message.start()
    
    Thread(target=consumer_score, 
           args=(fifo_message, fifo_score, TOTAL_CAPACITORS), 
           name="thread_monitor").start()

    Thread(target=consumer_error, 
           args=(fifo_error,), 
           name="thread_error").start()

    for i in range(TOTAL_CAPACITORS):

        Thread(target=producer_flux, 
               args=(fifo_message, fifo_score, randrange(1, 9), TOTAL_CAPACITORS, get_estrategy()), 
               name=f"flux_{i}").start()
        
        time.sleep(.1)

    # thread_message.join()
    thread_spinner.join()