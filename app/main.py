import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        sys.stdout.write(user_input + ": " + "command not found" + "\n")

if __name__ == "__main__":
    main()
