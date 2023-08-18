from time import sleep
from threading import Event, Thread
from collections import deque

from core.flux_core import flux_producer
from core.expedition_core import expedition_config, launch_expedition
from infra.db.sqlite_db import connection_db
from consumers.progress_spinner import progress_consumer
from consumers.flux_consumer import flux_consumer


def thread_capacitor() -> None:

    event: Event = Event()

    signals_process = deque()

    flux_message = deque()

    TOTAL_CAPACITORS: int = 10

    thread_progress = Thread(target=progress_consumer,
                             args=(event,
                                   signals_process,
                                   TOTAL_CAPACITORS),
                             name="thread_spinner")

    thread_progress.start()

    Thread(target=flux_consumer,
           args=(event, flux_message, "", connection_db),
           name="thread_message").start()

    for i in range(TOTAL_CAPACITORS):

        Thread(target=flux_producer,
               args=(event,
                     flux_message,
                     signals_process,
                     expedition_config,
                     launch_expedition),
               name=f"flux_{i}").start()

        sleep(.1)

    thread_progress.join()
