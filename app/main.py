import sys
import os
import subprocess

def is_executable(program):
    path_dirs = os.environ.get('PATH').split(os.pathsep)

    for directory in path_dirs:
        path = os.path.join(directory, program)

        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path

    return None

def main():

    builtin = {"type", "echo", "exit", "pwd", "cd"}
 
    while True:

        user_input = input("$ ").split()
        command = user_input[0]
        path = is_executable(command)

        match command:

            case "exit":
                sys.exit()

            case "echo":
                sys.stdout.write(" ".join(user_input[1:]) + "\n")
                
            case "type":
                for val in user_input[1:]: 
                    if val in builtin:
                        sys.stdout.write(val + " is a shell builtin" + "\n")
                        continue
                    
                    val_path = is_executable(val)

                    if val_path:
                        sys.stdout.write(val + " is " + val_path + "\n")     
                    else:
                        sys.stdout.write(val + ": not found" + "\n")

            case _ if path:
                subprocess.run([command] + user_input[1:]) 

            case "pwd":
                sys.stdout.write(os.getcwd() + "\n")
 
            case "cd":
                if user_input[1]:
                    if user_input[1] == "~":
                        os.chdir(os.getenv('HOME'))
                    elif os.path.isdir(user_input[1]):
                        os.chdir(user_input[1])
                    else:
                        sys.stdout.write("cd: " + user_input[1] + ": No such file or directory" + "\n") 
                
            case _:
                sys.stdout.write(command + ": command not found" + "\n")
        
if __name__ == "__main__":
    main()
