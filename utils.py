
def readfile(filename):
    with open(filename, 'r') as filehandle:
        filecontent = filehandle.read()
    return filecontent