import olefile
import binascii
import sys

def searchHelper(dir, value):
    result = []
    contains = []
    for i in range(0, len(dir)):
       curr = dir[i]
       currVal = curr[len(curr) - 1]
       if value.lower() in currVal.lower():
        contains.append(curr)
        if currVal.lower() == value.lower():
            result = curr
    return {'path': result, 'contains': contains}

def search(ole, value):
    dir = ole.listdir()
    result = searchHelper(dir, value)
    path = result['path']
    contains = result['contains']
    if len(path) == 0:
        print '\'' + value + '\' was not found but the following contain \'' + value + '\':'
        for i in range(0, len(contains)):
            path = contains[i]
            print convertPathToString(path) 
    else:
        for i in range(0, len(contains)):
            currPath = contains[i]
            lastVal = currPath[len(currPath)-1]
            if lastVal.lower() == value.lower():
                valOfStream = getVal(ole, currPath)
                print pathWithVal(currPath, valOfStream)
        valOfStream = getVal(ole, path)
        #print pathWithVal(path, valOfStream)

def getVal(ole, path):
    if len(path) > 0:
         result = str(ole.openstream(path).read())
         return result
    else:
        return ''

def convertPathToString(path):
    result = '';
    if len(path) > 0:
        result += path[0]
        for i in range(1, len(path)):
            result += ' -> ' + path[i]

    return result

def pathWithVal(path, value):
    return convertPathToString(path) + '\t value: 0x' + binascii.hexlify(value)
        

def main():
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        ole = olefile.OleFileIO(filename)
        search(ole, sys.argv[2])
    else:
        print "Missing the search value argument"
    
if __name__ == "__main__":
    main()
