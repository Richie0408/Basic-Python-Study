answer = input("> ")
while answer.upper() != "QUIT":
    if answer.upper() == "HELP":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit",'\n')
        answer = input("> ")
    elif answer.upper() == "START":
        print("Car started... Ready to go !",'\n')
        answer = input("> ")
    elif answer.upper() == "STOP":
        print("Car stopped.",'\n')
        answer = input("> ")
    elif answer.upper() == "QUIT":
        break
    else:
        print("I don't understand that...",'\n')
        answer = input("> ")


