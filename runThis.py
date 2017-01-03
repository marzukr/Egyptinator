import egyptC0re,sys

print("\nEGYPTINATOR\u2122 2000 ENCODING MACHINE")
print("------------------------------------\n")

while True:
    data = input("Egyptinator:~ User$ ")
    if data == "egyptIt" or data == "degyptIt":
        print("(*) indicates default.")
        egyptType = input("E2(*) or E1: ")
        if egyptType == "":
            egyptType = "E2"
        elif egyptType.lower() != "e1" and egyptType.lower() != "e2":
            print("Invalid option")
            continue
        option = input("Message(*) or File: ")
        if option.lower() == "message" or option == "":
            message = input("Message: ")
        elif option.lower() == "file":
            fileLoc = input("Location: ")
            try:
                f = open(fileLoc, "r")
                message = f.read()
                f.close()
            except Exception:
                print("Invalid File/Location")
                continue
        else:
            print("Invalid Option")
            continue
        key = input("Key: ")
        mainP = egyptC0re.Processor(key, message)
        print("Output: ")
        result = ""
        result = mainP.egyptIt(egyptType, data)
        if option == "file" and result is not "ERROR":
            f = open(fileLoc, "w")
            f.write(result)
            f.close()
            print("Result written to file")
        else:
            print(result)
        continue
    elif data == "":
        continue
    elif data == "help" or data == "shutdown" or data == "clear":
        if data == "help":
            print("Commands Available: egyptIt, degyptIt, help, shutdown, clear")
        elif data == "shutdown":
            sys.exit(0)
        elif data == "clear":
            for n in range(0,50):
                print("\n")
        continue
    else:
        print("Command not recognized")
        continue
