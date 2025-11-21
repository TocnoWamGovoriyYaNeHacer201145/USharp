import random
import time
import subprocess
import sys
import os

# Symbols list and variables dict
symbols=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','0','1','2','3','4','5','6','7','8','9']
variables={}

# Main Interpreter, processes argument with many if, elif
def MainInterpreter(command):
    if command.startswith('I_AM_XD') and command.endswith(';'):
        print("I am XD too")
    elif command.startswith('printu("') and command.endswith('");'):
        print(command[8:-3])
    elif 'random_number' in command and command.startswith('random') and command.endswith('_number;'):
        print(random.randint(1, 9999999999))
    elif 'random_symbols' in command and command.startswith('random') and command.endswith('_symbols;'):
        print_content = []
        for i in range(random.randint(1, 99)):
            print_content.append(random.choice(symbols))
        print(''.join(print_content))
    elif 'wait' in command and command.startswith('wait(') and command.endswith(');'):
        wait_time=int(command[5:-2])
        time.sleep(wait_time)
    elif 'pycommand' in command and command.startswith('pycommand(') and command.endswith(');'):
        result=eval(command[10:-2])
        print(result)
    elif 'terminal_command' in command and command.startswith('terminal_command(') and command.endswith(');'):
        subprocess.run(command[17:-2], shell=True)
    elif command.startswith(('public', 'static', 'dynamic', 'void', 'namespace', '//')):
        pass
    elif command.startswith('using') and command.endswith(';'):
        print(f'Imported module {command[6:-1]}')
    elif command.startswith('Console.WriteLine(') and command.endswith(');'):
        argument = command[command.find('(') + 1:command.find(')')]
        if argument != None: print(argument)
        else: print()
    elif command.startswith('Console.Write(') and command.endswith(');'):
        argument = command[command.find('(') + 1:command.find(')')]
        print(argument[1:-1], end='')
    elif command.startswith('CreateFile(') and command.endswith(');'):
        if os.path.exists(command[12:-3]) == True:
            print(f'Failed to create file {command[12:-3]}, file already exists')
        else:
            try:
                open(command[12:-3], 'w')
            except OSError:
                print(f'Failed to create file {command[12:-3]}\nError: {Exception}')
    elif command.startswith('ClearFile(') and command.endswith(');'):
        if os.path.exists(command[11:-3]) == True:
            try:
                open(command[11:-3], 'w')
            except OSError:
                print(f'Failed to delete file {command[11:-3]}\nError: {Exception}')
        else:
            print(f'File {command[11:-3]} does not exists')
    elif command.startswith('DeleteFile(') and command.endswith(');'):
        if os.path.exists(command[12:-3]):
            try:
                os.remove(command[12:-3])
            except OSError:
                print(f'Failed to delete file {command[12:-3]}\nError: {Exception}')
        else:
            print(f'File {command[12:-3]} does not exists')
    elif '=' in command and command.endswith(';'):
        newvar=command[:-1].split('=')
        if ' ' in newvar[0]:
            newvar[0]=newvar[0].replace(' ', '')
            if ' ' in newvar[1]:
                if ['1','2','3','4','5','6','7','8','9'] in newvar and not symbols in newvar: 
                    int(newvar[1])
                newvar[1]=newvar[1].replace(' ', '')
        variables[newvar[0]] = newvar[1]
    elif command.startswith('GetType(') and command.endswith(');'):
        print(type(command[8:-2])) 
    else:
        print(f"I don't understand {command}")

# Function, that processes lines of a file and gives them as argument to MainInterpreter
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
