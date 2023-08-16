import time
from itertools import cycle
from collections import deque
from infra.log_system.logging_exception import  inject_error

def fifo_deque():

    fifo_status_percent = deque()

    fifo_message = deque()

    fifo_score = deque()

    fifo_error = deque()

    def consumer_error(fifo_error:deque) -> None:

        while True:

            if fifo_error:
                
                inject_error(fifo_error.popleft())

    def consumer_message(fifo_status_percent:deque, fifo_message:deque, total_capacitors:int) -> None:
        
        counter:int = 0

        while counter < total_capacitors:

            if fifo_message:

                data:tuple = fifo_message.popleft()

                if "EXITING" == data[1].upper():
                    counter += 1
                    fifo_status_percent.appendleft(int((counter / total_capacitors) * 100))
            
            time.sleep(0.1)


    def consumer_score(fifo_message, fifo_score:deque, total_capacitors:int) -> None:

        counter:int = 0 

        while counter < total_capacitors:

            if fifo_score:                

                data = fifo_score.popleft()

                with open("score.txt", "a") as f:
                    f.write(f"{data[0]}-{data[1]}\n")

                fifo_message.appendleft((data[0], f"Score armazenado:{data[1]}"))

                counter +=1 

                data.release()

            time.sleep(0.1)
                
    def consumer_spinner(fifo_counter_processed:deque, total_capacitors:int) -> None:
        
        counter_processed:int = 0
        perc: int = 0
        hide_curor:str = '\033[?25l'
        
        for char in cycle('|/-\\'):

            if fifo_counter_processed:
                counter_processed += fifo_counter_processed.popleft()
                perc = int((counter_processed / total_capacitors) * 100)

            print(end=f"{hide_curor}{'processed' if perc == 100 else 'processing'}...{char} {perc}%\r")
            time.sleep(.08)
            
            if counter_processed >= total_capacitors:
                break

    return fifo_status_percent, \
        fifo_message, \
            fifo_score, \
                fifo_error, \
                    consumer_spinner, \
                        consumer_message, \
                            consumer_score, \
                                consumer_error
