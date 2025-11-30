import random
import time
import sys
import subprocess
import re
import py_compile
import os

symbols=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','0','1','2','3','4','5','6','7','8','9']
compiled_filename = None

# Command dictionary
command_dict = {
    "I_AM_XD": "print('I am XD too...')",
    "int": "",
    "string": "",
    "bool": "",
    "float": "",
    "void": "def",
    "printu": "print", 
    "Console.WriteLine": "print",
    "random_number": "print(random.randint(1, 9999999999))",
    "random_symbols": f"print_content = []\nfor i in range(random.randint(1, 99)): print_content.append(random.choice(symbols))\nprint(''.join(print_content))",
    "wait": "time.sleep",
    "terminal_command": "subprocess.run",
    "using": "import",
    "//": "#",
    ";": "",
    "public": "", "private": "", "static": "", "dynamic": "",
    "++": "+= 1",
    "--": "-= 1"
}

def command_parser(content):
    mod_content = content
    for command in command_dict:
        if command and (command[0].isalnum() or command[0] == '_'):
            pattern = r'\b' + re.escape(command) + r'\b'
        else: pattern = re.escape(command) 
        mod_content = re.sub(pattern, command_dict[command], mod_content)
    open(temp_filename, 'w').write(mod_content)
    try:
        py_compile.compile(temp_filename, cfile=compiled_filename)
        try:
            os.remove(temp_filename)
        except:
            print(f'Failed to delete temp file {temp_filename}')
    except Exception as e:
        print(f'Failed to compile file: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: <interpreter name> <your .usharp file path>")
        sys.exit(1)
    file_template = sys.argv[1].replace('.usharp', '')
    temp_filename = file_template + '.py'
    compiled_filename = file_template + '.usc'
    with open(sys.argv[1], 'r') as file:
        command_parser(file.read())
