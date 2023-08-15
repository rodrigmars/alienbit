from thread_capacitors import thread_capacitor

def main() -> None:thread_capacitor()

if __name__ == "__main__":

    try:

        main()

    except Exception as e:
        print(e)
        exit(1)    
    else:
        print("Capacitores processados com sucesso")
    finally:
        exit(0)
