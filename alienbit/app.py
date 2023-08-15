from thread_capacitors import thread_capacitor

def main() -> None:thread_capacitor()

if __name__ == "__main__":

    try:

        main()

        print("Capacitores processados com sucesso")

        exit(0)

    except Exception as e:
        
        print(e)
        
        exit(1)