import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    user_input = input()
    sys.stdout.write(user_input + ": " + "command not found" + "\n")
    pass


if __name__ == "__main__":
    main()
