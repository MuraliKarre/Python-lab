command = ""
started = False
while True:
    command  =input ("> ").lower()
    if command == "start":
        if started:
            print("Car is already started...")
        else:
            started = True    
            print("Car Started ....")
    elif command == "stop":
        if not started:
            print("Car is already stop..")
        else:
            started = False
            print("Stop Car.....")
    elif command == "help":
        print(""" 
start - To start car
stop - To stop car
quit - To exit
        """)
    elif command == "quit":
        print("to exit ...")
        break
else:
    print("Sorry idon't understand your command")