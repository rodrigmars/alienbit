from threading import Event, current_thread
from collections import deque
from random import randrange, choice

def flux_producer(event:Event, flux_message:deque, signals_process:deque, total_time:int):

    def get_estrategy():
        def gera_quantidade(x:int, y:int) -> int :return randrange(x, y)
        return {"ranks":choice([{"rank":["A", gera_quantidade(6000, 9999)]},
                 {"rank":["B", gera_quantidade(4000, 6000)]},
                 {"rank":["C", gera_quantidade(3000, 4500)]},
                 {"rank":["D", gera_quantidade(2500, 3500)]},
                 {"rank":["E", gera_quantidade(1500, 2100)]}]),
        "rocks":choice(["Silicate", "Platinum", "Cobalt", "Iron", "Nickel"]),
        "economys":choice([{"strong": 8}, {"weak":4}, {"average":2}])}

    def hard_verse(economy:str):
        def x_play(ranks:list):
            def y_stop(rocks:list):
                def z_pause(economys:list):
                    return "teste"
                return z_pause
            return y_stop
        return x_play

    status:str="Starting"
    
    messages = []

    try:

        flux_message.appendleft({"LOG_INFO": (current_thread().name, status)})

        event.wait(total_time)

        strategy = get_estrategy()
        
        score = hard_verse(strategy["economy"])(strategy["coin"])(strategy["economy_"])(strategy["percent"])

        # messages.append({"SCORE": (current_thread().name, score)})
        flux_message.appendleft({"SCORE": (current_thread().name, score)})

        status = "Processed"

        event.wait(.1)

    except Exception as e:
    
        flux_message.appendleft({"ERROR": (current_thread().name, e)})
        
        status = "Processed with Error"
    
    finally:
        
        # flux_message.appendleft(messages)
        
        flux_message.appendleft({"LOG_INFO": (current_thread().name, status)})
        
        signals_process.appendleft(1)
        
        messages.clear()

        
