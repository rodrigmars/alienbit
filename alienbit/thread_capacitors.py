import time
from random import randrange
from fifo import fifo_deque
from threading import Event, Thread
from core.flux_core import producer_flux
from core.verse_core import hard_verse, get_estrategy

def thread_capacitor() -> None:

    fifo_signals_process, \
        fifo_message, \
            fifo_score, \
                fifo_error, \
                    consumer_spinner, \
                        consumer_message, \
                            consumer_score, \
                                consumer_error = fifo_deque()

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
               args=(event, fifo_message, fifo_score, fifo_signals_process, randrange(1, 9), hard_verse, get_estrategy()), 
               name=f"flux_{i}").start()
        
        time.sleep(.1)

    print(fifo_error.popleft)

    thread_spinner.join()