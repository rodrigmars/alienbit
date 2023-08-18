from typing import Callable
from threading import Event, current_thread
from collections import deque

def flux_producer(event:Event, 
                  flux_message:deque, 
                  signals_process:deque, 
                  expedition_config:Callable[[], tuple], 
                  launch_expedition:Callable[[Event, deque, dict], Callable[[list], Callable]]):

    status:str="Starting"
    
    messages = []

    try:

        flux_message.appendleft({"LOG_INFO": (current_thread().name, status)})

        # event.wait(total_time)

        spaceship, rock, warp_jump, economy = expedition_config()

        expedition = launch_expedition(event, flux_message, spaceship)(rock)(warp_jump)(economy)
        
        flux_message.appendleft({"SCORE": (current_thread().name, expedition)})

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

        
