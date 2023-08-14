def hard_verse(track:str):

    def x_play(x):
        def y_stop(y:list):
            def z_pause(z):
                return "teste"
            return z_pause
        return y_stop
    return x_play

def flux_01(fifo_message, fifo_score, wait:int):

    fifo_message.appendleft((current_thread().name, 'Starting'))

    time.sleep(wait)
    score = hard_verse("sadsa")(25)([.1, 25])(2.5)

    fifo_score.appendleft((current_thread().name, f'score:{score}'))

    time.sleep(.5)

    fifo_message.appendleft((current_thread().name, 'Exiting'))

def consumer_message(fifo_message) -> None:
    while True:

        if len(fifo_message) >= 1:

            data = fifo_message.popleft()

            print("Message:", data)

            if "end" == data:
                break

def consumer_score(fifo_message, fifo_score) -> None:

    counter = 0 

    while counter < 3:
        if len(fifo_score) >= 1:
            data = fifo_score.popleft()
            print("Score calculado:", data)
            counter +=1 

    fifo_message.appendleft("end")

if __name__ == "__main__":

    import time
    from collections import deque
    from threading import Thread, active_count, get_ident, current_thread

    fifo_message = deque()

    fifo_score = deque()

    capacitors:list = [[flux_01, 5, "flux_01"], [flux_01, 25, "flux_02"], [flux_01, 15, "flux_03"]]
    
    thread_message = Thread(target=consumer_message, args=(fifo_message,), name="thread_monitor")
    thread_message.start()
    
    thread_score = Thread(target=consumer_score, args=(fifo_message, fifo_score), name="thread_monitor")
    thread_score.start()
    
    for flux in capacitors:
        flux_read = Thread(target=flux[0], args=(fifo_message, fifo_score, flux[1]), name=flux[2])
        flux_read.start()

    thread_message.join()

    print("Capacitores processados com sucesso")