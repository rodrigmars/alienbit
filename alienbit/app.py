from time import perf_counter
from pathlib import Path
from traceback import format_exc
from thread_capacitors import thread_capacitor
from infra.log_system.logging_exception import  inject_error

if __name__ == "__main__":

    exit_code:int = 0

    try:
        start:float= perf_counter()

        # @lambda _: _()
        # def main() -> None: thread_capacitor()

        spaceship, rock, warp_jump, economy = expedition_config()

        score = launch_expedition(spaceship)(rock)(warp_jump)(economy)
        print("score:>", score)

    except Exception as e:
        inject_error(("module:app", format_exc()))

    else:
        
        elapsed:float = perf_counter() - start
        print(flush=True, end=f">> Capacitores processados com sucesso - tempo total:{elapsed:.2f}s")

    finally:

        exit(exit_code)
