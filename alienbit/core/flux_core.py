from threading import Event, current_thread
from collections import deque

def producer_flux(event:Event, fifo_message:deque, fifo_score:deque, fifo_signals_process:deque, total_time:int, hard_verse, strategy:dict):

    status:str=""

    try:

        fifo_message.appendleft((current_thread().name, 'Starting'))

        event.wait(total_time)

        score = hard_verse(strategy["economy"])(strategy["coin"])(strategy["economy_"])(strategy["percent"])

        fifo_score.appendleft((current_thread().name, f'score:{score}'))

        status = "Processed"

        event.wait(.1)

    except Exception as e:
        # fifo_error.appendleft((current_thread().name, 'Error', e))
        status = "Processed with Error"
    finally:
        fifo_message.appendleft((current_thread().name, status))
        fifo_signals_process.appendleft(1)
