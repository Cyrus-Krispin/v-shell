import sys


def main():

    while True:
        user_input = input("$ ").split()
        if user_input[0] == "exit":
            sys.exit()
        elif user_input[0] == "echo":
            sys.stdout.write(" ".join(user_input[1:]) + "\n")
        else:
            sys.stdout.write(" ".join(user_input) + ": command not found" + "\n")
        
        
if __name__ == "__main__":
    main()
