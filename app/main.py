import sys
import os
import subprocess
import shlex

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

        user_input = input("$ ")
        command, *args = shlex.split(user_input)
        path = is_executable(command)
        
        if ">" in args or "1>" in args or "2>" in args:
            os.system(user_input)
            continue

        match command:

            case "exit":
                sys.exit()

            case "echo":
                sys.stdout.write(" ".join(args) + "\n")
                
            case "type":
                for val in args: 
                    if val in builtin:
                        sys.stdout.write(val + " is a shell builtin" + "\n")
                        continue
                    
                    val_path = is_executable(val)

                    if val_path:
                        sys.stdout.write(val + " is " + val_path + "\n")     
                    else:
                        sys.stdout.write(val + ": not found" + "\n")

            case _ if path:
                subprocess.run([command] + args) 

            case "pwd":
                sys.stdout.write(os.getcwd() + "\n")
 
            case "cd":
                if user_input[1]:
                    if args[0] == "~":
                        os.chdir(os.getenv('HOME'))
                    elif os.path.isdir(args[0]):
                        os.chdir(args[0])
                    else:
                        sys.stdout.write("cd: " + args[0] + ": No such file or directory" + "\n") 
                
            case _:
                sys.stdout.write(command + ": command not found" + "\n")
        
if __name__ == "__main__":
    main()
