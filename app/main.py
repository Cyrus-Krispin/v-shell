import sys


def main():

    builtin = {"type", "echo", "exit"}

    while True:
        user_input = input("$ ").split()
        command = user_input[0]
        match command:
            case "exit":
                sys.exit()
            case "echo":
                sys.stdout.write(" ".join(user_input[1:]) + "\n")
            case "type":
                for val in user_input[1:]: 
                    if val in builtin:
                        sys.stdout.write(val + " is a shell builtin" + "\n") 
                    else:
                        sys.stdout.write(val + ": not found" + "\n")

 
            case _:
                sys.stdout.write(command + ": command not found" + "\n")
        
        
if __name__ == "__main__":
    main()
