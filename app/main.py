import sys
import os

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
                found = False
                for val in user_input[1:]: 
                    if val in builtin:
                        sys.stdout.write(val + " is a shell builtin" + "\n") 
                        found = True 
                    else:
                        path_dirs = os.environ.get('PATH').split(os.pathsep)
                        for di in path_dirs:
                            if os.path.isfile(di + "/" + val):
                                if os.access(di + "/" + val, os.X_OK):
                                    sys.stdout.write(val + " is " + di + "/" + val + "\n")
                                    found = True
                                    break
                    if not found:
                        sys.stdout.write(val + ": not found" + "\n")
 
            case _:
                sys.stdout.write(command + ": command not found" + "\n")
        
        
if __name__ == "__main__":
    main()
