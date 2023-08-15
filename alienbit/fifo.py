from os import system
import random
from collections import deque
import time
def fifo_deque():

    fifo_message = deque()

    fifo_score = deque()


    def consumer_message(fifo_message:deque, num_capacitors:int) -> None:
        
        counter:int = 0

        while counter < num_capacitors:
            time.sleep(0.1)
            if fifo_message:

                data = fifo_message.popleft()

                # print("Message:", data)

                if "Exiting" == data[1]:
                    counter += 1
                    perc = int((counter / num_capacitors) * 100)
                    system("cls")
                    animation:str = random.choice(['•','♦','►', '♣', '○', '▼'])
                    print(f"processing...{animation} {perc:0>2}%")
                    

    def consumer_score(fifo_message, fifo_score, num_capacitors:int) -> None:

        counter:int = 0 

        while counter < num_capacitors:
            time.sleep(0.1)
            if fifo_score:                

                data = fifo_score.popleft()

                with open("score.txt", "a") as f:
                    f.write(f"{data[0]}-{data[1]}\n")

                fifo_message.appendleft((data[0], f"Score armazenado:{data[1]}"))

                counter +=1 

    return fifo_message, fifo_score, consumer_message, consumer_score
