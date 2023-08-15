from collections import deque
import time

def fifo_deque():

    fifo_status_percent = deque()

    fifo_message = deque()

    fifo_score = deque()

    def consumer_message(fifo_status_percent:deque, fifo_message:deque, total_capacitors:int) -> None:
        
        counter:int = 0

        while counter < total_capacitors:

            if fifo_message:

                data = fifo_message.popleft()

                # print("Message:", data)

                if "Exiting" == data[1]:
                    counter += 1
                    fifo_status_percent.appendleft(int((counter / total_capacitors) * 100))
            
            time.sleep(0.1)

    def consumer_score(fifo_message, fifo_score, total_capacitors:int) -> None:

        counter:int = 0 

        while counter < total_capacitors:

            if fifo_score:                

                data = fifo_score.popleft()

                with open("score.txt", "a") as f:
                    f.write(f"{data[0]}-{data[1]}\n")

                fifo_message.appendleft((data[0], f"Score armazenado:{data[1]}"))

                counter +=1 

            time.sleep(0.1)
                
    def consumer_spinner(fifo_status_percent:deque) -> None:
        
        perc:int = 0
        hide_curor:str = '\033[?25l'
        while True:

            if fifo_status_percent:
                perc = fifo_status_percent.popleft()

            for char in '|/-\\':
                print(end=f"{hide_curor}{'processed' if 100 == perc else 'processing'}...{char} {perc}%\r")
                time.sleep(.08)
            
            if 100 == perc:
                break

    return fifo_status_percent, fifo_message, fifo_score, consumer_spinner, consumer_message, consumer_score
