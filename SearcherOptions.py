from Tkinter import Tk
from tkFileDialog import askopenfilename
import olefile
import SearcherModel

ole = None

def NewFile():
    Tk().withdraw()
    filename = askopenfilename()
    ole = olefile.OleFileIO(filename)
    print filename
    print 'NewFile()'
    return True

def Search():
    if ole == None:
        print 'No file has been selected'
    else:
        value = raw_input("Enter search value: ")
        SearcherModel.search(ole, value)
    print 'Search()'
    return True

def Exit():
    print 'Exit()'
    return False
