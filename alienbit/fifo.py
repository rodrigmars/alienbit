from collections import deque

def fifo_deque():

    fifo_message = deque()

    fifo_score = deque()


    def consumer_message(fifo_message:deque, num_capacitors:int) -> None:
        
        counter:int = 0

        while counter < num_capacitors:

            if fifo_message:

                data = fifo_message.popleft()

                print("Message:", data)

                if "Exiting" == data[1]:
                    counter += 1

    def consumer_score(fifo_message, fifo_score, num_capacitors:int) -> None:

        counter:int = 0 

        while counter < num_capacitors:

            if fifo_score:                

                data = fifo_score.popleft()

                fifo_message.appendleft((data[0], f"Score armazenado:{data[1]}"))

                counter +=1 

    return fifo_message, fifo_score, consumer_message, consumer_score
