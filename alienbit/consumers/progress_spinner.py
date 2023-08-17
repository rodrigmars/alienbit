from threading import Event
from itertools import cycle
from collections import deque
    
def progress_consumer(event:Event, fifo_signals_process:deque, total_capacitors:int) -> None:

    counter_processed:int = 0
    perc: int = 0
    hide_curor:str = '\033[?25l'
    
    for char in cycle('◰◳◲◱'):

        if fifo_signals_process:
            counter_processed += fifo_signals_process.popleft()
            perc = int((counter_processed / total_capacitors) * 100)

        processed = 'processed' if perc == 100 else 'processing'

        print(flush=True, end=f"{hide_curor}{processed}...{char} {perc}%\r")

        event.wait(.1)
        
        if counter_processed >= total_capacitors:
            event.set()
            break