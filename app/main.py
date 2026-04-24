import sys


def main():

    while True:
        user_input = input("$ ").split()
        if user_input[0] == "exit":
            sys.exit()
        if user_input[0] == "echo":
            if user_input[1:]:
                sys.stdout.write(" ".join(user_input[1:]) + "\n")
        
if __name__ == "__main__":
    main()
