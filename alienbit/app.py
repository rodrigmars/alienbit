from collections import deque

def hard_verse(track:str):

    def x_play(x):
        def y_stop(y:list):
            def z_pause(z):
                return "teste"
            return z_pause
        return y_stop
    return x_play

def producer_flux(fifo_message:deque, fifo_score:deque, total_time:int):

    fifo_message.appendleft((current_thread().name, 'Starting'))

    time.sleep(total_time)

    score = hard_verse("sadsa")(25)([.1, 25])(2.5)

    fifo_score.appendleft((current_thread().name, f'score:{score}'))

    time.sleep(.1)

    fifo_message.appendleft((current_thread().name, 'Exiting'))

def consumer_message(fifo_message:deque, num_capacitors:int) -> None:
    
    counter:int = 0

    while counter < num_capacitors:

        if len(fifo_message) >= 1:

            data = fifo_message.popleft()

            print("Message:", data)

            if "Exiting" == data[1]:
                counter += 1

def consumer_score(fifo_message, fifo_score, num_capacitors:int) -> None:

    counter:int = 0 

    while counter < num_capacitors:

        if len(fifo_score) >= 1:

            data = fifo_score.popleft()

            fifo_message.appendleft((data[0], f"Score armazenado:{data[1]}"))

            counter +=1 

if __name__ == "__main__":

    import time
    
    from threading import Thread, current_thread

    fifo_message = deque()

    fifo_score = deque()

    capacitors:list = [[ producer_flux, 2, "flux_01"], 
                       [ producer_flux, 2, "flux_02"], 
                       [ producer_flux, 1, "flux_03"]]

    thread_message = Thread(target=consumer_message, args=(fifo_message, len(capacitors)), name="thread_monitor")
    thread_message.start()
    
    thread_score = Thread(target=consumer_score, args=(fifo_message, fifo_score, len(capacitors)), name="thread_monitor")
    thread_score.start()
    
    for flux in capacitors:
        flux_read = Thread(target=flux[0], args=(fifo_message, fifo_score, flux[1]), name=flux[2])
        flux_read.start()

    thread_message.join()

    print("Capacitores processados com sucesso")