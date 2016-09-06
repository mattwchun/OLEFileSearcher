from Tkinter import Tk
from tkFileDialog import askopenfilename

def NewFile():
    Tk().withdraw()
    filename = askopenfilename()
    print filename
    print 'NewFile()'
    return True

def Search():
    print 'Search()'

def Exit():
    print 'Exit()'
