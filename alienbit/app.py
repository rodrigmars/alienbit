from thread_capacitors import thread_capacitor

def main() -> None:thread_capacitor()

if __name__ == "__main__":

    try:

        from threading import Event, Thread
        from itertools import cycle
        import time
        
        event = Event()

        def teste(event:Event):
            total = 0
            for char in cycle('◰◳◲◱'):
                total +=1 
                print(f"Resultado:{total:03} {char}", flush=True, end='\r')
                if event.wait(.1):
                # if event.is_set():
                    break

        Thread(target=teste, args=(event,)).start()

        time.sleep(5)
        event.set()
        print("Programa finalizado")
        # main()

    except Exception as e:
        print(e)
        exit(1)    
    else:
        print("\nCapacitores processados com sucesso")
    finally:
        exit(0)
