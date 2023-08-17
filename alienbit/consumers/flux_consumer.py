from typing import Callable
from threading import Event
from collections import deque
from sqlite3 import Connection

def flux_consumer(event:Event, 
                flux_message:deque, 
                path_db:str, 
                connection_db:Callable[[str], Callable[[], Connection]]) -> None:
       
    try:

        with connection_db(path_db)() as conn:
            
            cursor = conn.cursor()

            while True:

                if flux_message:
                    
                    message = flux_message.popleft()
                    
                    cursor.execute("INSERT INTO TEMP_ERRORS VALUES (num_errors)")
                    # cursor.execute("INSERT INTO ERRORS VALUES ()")

                    conn.commit()        

                if event.wait(.1):
                    break
    except Exception as e:
        ...