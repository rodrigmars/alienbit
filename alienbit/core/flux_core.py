from threading import Event, current_thread
from collections import deque
from random import randrange, choice

def producer_flux(event:Event, flux_message:deque, signals_process:deque, total_time:int):

    def get_estrategy():
        return {"economy":choice(["strong", "weak", "average"]),
        "coin": randrange(1000, 9000),
        "economy_": choice([[.1, 25], [.1, 25], [.1, 25]]),
        "percent": choice([0.5, 1.5, 3.1, 5.4, 8.9])}

    def hard_verse(economy:str):

        def x_play(x):
            def y_stop(y:list):
                def z_pause(z):
                    return "teste"
                return z_pause
            return y_stop
        return x_play

    status:str="Starting"
    
    messages = []

    try:

        messages.append({"LOG_INFO": (current_thread().name, status)})

        event.wait(total_time)

        strategy = get_estrategy()
        
        score = hard_verse(strategy["economy"])(strategy["coin"])(strategy["economy_"])(strategy["percent"])

        messages.append({"SCORE": (current_thread().name, score)})

        status = "Processed"

        event.wait(.1)

    except Exception as e:
    
        messages.append({"ERROR": (current_thread().name, e)})
        
        status = "Processed with Error"
    
    finally:
        
        messages.append({"LOG_INFO": (current_thread().name, status)})
        
        flux_message.appendleft(messages)

        signals_process.appendleft(1)
