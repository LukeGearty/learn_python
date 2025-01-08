import sys
import time


def stop_watch():
    print("Starting clock now, press 2 to stop the watch!: ")

    #start clock

    start_time = time.time()

    while True:
        try:
            #user input
            choice = int(input("Press 2 to stop the watch: "))
            if choice == 2:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds")
                break
            else:
                print("Invalid choice, press 2 to stop the watch.")
        except ValueError:
            print("Please press a number, nothing else")


def main():
    print("Press 1 to start clock, 2 to exit")

    try:
        choice = int(input())
        while choice not in [1, 2]:
            print("Invalid choice, press 1 or 2: ")
            choice = int(input())
        
        if choice == 1:
            stop_watch()
        elif choice == 2:
            sys.exit()
    except ValueError:
        print("Please press a number, nothing else: ")
        choice = int(input())

if __name__=="__main__":
    main()