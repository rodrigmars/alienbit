from threading import Event
from itertools import cycle
from collections import deque
from infra.log_system.logging_exception import  inject_error

def fifo_deque():

    fifo_signals_process = deque()

    fifo_message = deque()

    fifo_score = deque()

    fifo_error = deque()

    def consumer_error(event:Event, fifo_error:deque) -> None:

        conn: sqlite3.Connection | None = None

        try:

            conn = sqlite3.connect(':memory:') 

            cursor = conn.cursor()

            num_errors:int = 0

            while True:

                if fifo_error:
                    num_errors += 1 
                    # inject_error(fifo_error.popleft())
                    cursor.execute("INSERT INTO TEMP_ERRORS VALUES (num_errors)")
                    # cursor.execute("INSERT INTO ERRORS VALUES ()")

                    conn.commit()        

                if event.wait(.1):
                    break

        except Exception as e:
            ...

        finally:

            if conn:
                conn.close()

    def consumer_message(event:Event, fifo_message:deque) -> None:

        while True:

            if fifo_message:

                data:tuple = fifo_message.popleft()

                # if "EXITING" == data[1].upper():
                #     counter += 1
                #     fifo_status_percent.appendleft(int((counter / total_capacitors) * 100))
            
            if event.wait(.1):
                break

    def consumer_score(event:Event, fifo_message, fifo_score:deque) -> None:

        while True:

            if fifo_score:                

                data = fifo_score.popleft()

                with open("score.txt", "a") as f:
                    f.write(f"{data[0]}-{data[1]}\n")

                fifo_message.appendleft((data[0], f"Score armazenado:{data[1]}"))

            if event.wait(.1):
                break

    def consumer_spinner(event:Event, fifo_signals_process:deque, total_capacitors:int) -> None:

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

    return fifo_signals_process, \
        fifo_message, \
            fifo_score, \
                fifo_error, \
                    consumer_spinner, \
                        consumer_message, \
                            consumer_score, \
                                consumer_error
