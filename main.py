import random
import time
import subprocess
import sys

symbols=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','0','1','2','3','4','5','6','7','8','9']

def MainInterpreter(command):
    if command.startswith('I_AM_XD') and command.endswith(';'):
        print("I am XD too")
    elif command.startswith('printu("') and command.endswith('");'):
        print(command[7:-2])
    elif 'random_number' in command and command.startswith('random') and command.endswith('_number;'):
        print(random.randint(1, 9999999999))
    elif 'random_symbols' in command and command.startswith('random') and command.endswith('_symbols;'):
        print_content = []
        for i in range(random.randint(1, 99)):
            print_content.append(random.choice(symbols))
        print(''.join(print_content))
    elif 'wait' in command and command.startswith('wait(') and command.endswith(');'):
        wait_time=int(command[5:6])
        time.sleep(wait_time)
    elif 'pycommand' in command and command.startswith('pycommand(') and command.endswith(');'):
        result=eval(command[10:-1])
        print(result)
    elif 'terminal_command' in command and command.startswith('terminal_command(') and command.endswith(');'):
        subprocess.run(command[15:-1])
    elif command.startswith(('public', 'static', 'dynamic', 'void', 'namespace')):
        pass
    elif 'using' in command and command.startswith('using') and command.endswith(';'):
        print(f'Imported module {command[6:-1]}')
    elif command.startswith('#'):
        pass
    else:
        print(f"I don't understand {command}")

def ProcessFile(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                MainInterpreter(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <interpreter name> <your .usharp file path>")
        sys.exit(1)
    filepath=sys.argv[1]
    ProcessFile(filepath)
