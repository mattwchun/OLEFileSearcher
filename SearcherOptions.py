#from Tkinter import Tk
#from tkFileDialog import askopenfilename
import olefile
import SearcherModel

ole = None

def NewFile():
    #Tk().withdraw()
    #filename = askopenfilename()
    filename = raw_input("Enter valid relative path to OLE file: ")
    global ole
    ole = olefile.OleFileIO(filename)
    return True

def Search():
    if ole == None:
        print 'No file has been selected'
    else:
        value = raw_input("Enter search value: ")
        SearcherModel.search(ole, value)
    return True

def Exit():
    return False
