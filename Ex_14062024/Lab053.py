# Multiple conditions
# We use Switch for multipal conditions

number = int(input("Enter a number\n"))
match number:
    case 1:
        print("you entr number 1")

    case _:
        print("No idea")
