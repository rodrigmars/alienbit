import time
from threading import Event, Thread, current_thread
from collections import deque
from random import randrange, choice
from fifo import fifo_deque
from core import get_estrategy, hard_verse

def thread_capacitor() -> None:
    
    fifo_signals_process, \
        fifo_message, \
            fifo_score, \
                fifo_error, \
                    consumer_spinner, \
                        consumer_message, \
                            consumer_score, \
                                consumer_error = fifo_deque()


    def producer_flux(event:Event, fifo_message:deque, fifo_score:deque, fifo_signals_process:deque, total_time:int, strategy:dict):

        status:str=""

        try:

            fifo_message.appendleft((current_thread().name, 'Starting'))

            event.wait(total_time)

            score = hard_verse(strategy["economy"])(strategy["coin"])(strategy["economy_"])(strategy["percent"])

            fifo_score.appendleft((current_thread().name, f'score:{score}'))

            status = "Processed"

            event.wait(.1)

        except Exception as e:
            fifo_error.appendleft((current_thread().name, 'Error', e))
            status = "Processed with Error"
        finally:
            fifo_message.appendleft((current_thread().name, status))
            fifo_signals_process.appendleft(1)

    TOTAL_CAPACITORS:int = 10

    event:Event = Event()

    thread_spinner = Thread(target=consumer_spinner, 
                            args=(event, fifo_signals_process, TOTAL_CAPACITORS), 
                            name="thread_spinner")

    thread_spinner.start()

    Thread(target=consumer_message, 
                            args=(event, fifo_message), 
                            name="thread_message").start()
    
    Thread(target=consumer_score, 
           args=(event, fifo_message, fifo_score), 
           name="thread_monitor").start()

    Thread(target=consumer_error, 
           args=(event, fifo_error,), 
           name="thread_error").start()

    for i in range(TOTAL_CAPACITORS):

        Thread(target=producer_flux, 
               args=(event, fifo_message, fifo_score, fifo_signals_process, randrange(1, 9), get_estrategy()), 
               name=f"flux_{i}").start()
        
        time.sleep(.1)

    thread_spinner.join()