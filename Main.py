import SearcherModel
import SearcherOptions
import sys


def printMenuOptions():
    print 'Choose a Menu Option'
    print '(1) Enter File'
    print '(2) Search'
    print '(3) Exit'

# returns true if should ask again and false otherwise
def askOnce():
    printMenuOptions()
    resp = raw_input("Enter Menu Option: ")
    return handleResponse(int(resp))
    
def start():
    while askOnce():
        print '\n'
    
# returns true if should ask again and false otherwise
def handleResponse(response):
    result = True
    if response == 1:
        result = SearcherOptions.NewFile()
    elif response == 2:
        result = SearcherOptions.Search()
    elif response == 3:
        result = SearcherOptions.Exit()
    else:
        print 'Not an option'
        result = False
    return result

def NewFile():
    file = raw_input("Enter Relative Filepath: ")
    print file

def Search():
    print 'Search()'

options = {
    1: NewFile,
    2: Search
}

def main():
   if len(sys.argv) == 1:
    start()
   else:
    SearcherModel.main()

if __name__ == "__main__":
    main()
