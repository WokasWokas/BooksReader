try:
    import os
    def clearScreen(): return os.system('cls' if os.name=='nt' else 'clear')
    import sys
    def currentDir(): return os.path.abspath(__file__)
except ModuleNotFoundError as error:
    exit(error)

### settings ###
PATH = '\\'.join([elem for elem in currentDir().split('\\') if elem != 'main.py'])
commands = [['getbooks', 'Return list with books'], ['openbook', 'Open book'], ['help', 'Get help menu'], [ 'clear', 'Clear console'], ['exit', 'Close program']]
### functions ###
def getSpace(minValue: int, maxValue: int = 15):
    return ' ' * (maxValue - minValue)

def checkFolder():
    if os.path.isdir(f'{PATH}\\books') == True:
        return
    else:
        try:
            os.makedirs(name='books', mode=0o777, exist_ok=False)
        except OSError as error:
            exit(error)

def getHelp():
    print('#', 'command' + getSpace(len('command')), 'info')
    for command in commands: print('#' if command[0] == 'help' or command[0] == 'exit' or command[0] == 'clear' else commands.index(command) + 1, 
                    command[0] + getSpace(len(command[0])), command[1])

def getBooks():
    books = os.listdir(f'{PATH}\\books')
    print('#', 'book')
    for book in books: print(books.index(book) + 1, book.split('.')[0])

def openBook():
    name = input(f'Name > ')
    if os.path.isfile(f'{PATH}\\books\\{name}.txt') == True:
        with open(f'{PATH}\\books\\{name}.txt', 'r') as book:
            content = book.read().split('\n')
        for line in content: 
            if line.split(' ')[0] == '#': 
                print(getSpace(5), ' '.join([elem for elem in line.split(' ') if line.index(elem) != 0]))
                continue
            print(line)

def checkOption(option:str):
    if option == 'help': return getHelp()
    elif option == 'clear': clearScreen()
    elif option == 'exit': exit('User close program')
    elif option == '1' or option == 'getbooks': getBooks()
    elif option == '2' or option == 'openbook': openBook()

def main():
    checkFolder()
    clearScreen()
    while True:
        option = input(' > ')
        checkOption(option)

try:
    main()
except KeyboardInterrupt:
    print('\nUser close program')
