import os
import sys
import platform

def getData():
    i = 1
    mode = ""

    if platform.system == "Linux":
        directory = "./"
    else:
        directory = ".\\"
    
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == "directory" and len(sys.argv) > i + 1:
            directory = sys.argv[i + 1]
            i += 1
        elif arg == "mode" and len(sys.argv) > i + 1:
            mode = sys.argv[i + 1]
            i += 1

        i += 1

    return directory, mode

def getFilesArray(directory):
    filez = []

    for root, dirs, files in os.walk(directory):
        for f in files:
            filez.append(os.path.join(root, f))

    return filez

def getFilesTopDown(directory):
    for root, dirs, files in os.walk(directory):
        for f in files:
            print(f'{os.path.basename(root)}/{f}')

def getFilesTree(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)

        for f in files:
            print(f'{subindent}{f}')

def getTotalLines(files):
    lines = 0

    for f in files:
        lines += countLinesInFile(f)

    print(lines)

def countLinesInFile(filename):
    i = -1
    try:
        with open(filename, "r") as file:
            for i, l in enumerate(file):
                pass
    except UnicodeDecodeError:
        print(f"Warning: did not process file: {filename} as valid Unicode text.")
        return 0

    print(f"Counted {i+1} lines in file {filename}.")
    return i + 1

def main():
    directory, mode = getData()
    try:
        if mode == "getFilesArray":
            print(getFilesArray(directory))
        elif mode == "getFilesTopDown":
            getFilesTopDown(directory)
        elif mode == "getFilesTree":
            getFilesTree(directory)
        elif mode == "countFiles":
            print(len(getFilesArray(directory)))
        elif mode == "countTotalLines":
            getTotalLines(getFilesArray(directory))
        elif mode == "countLinesInFile":
            countLinesInFile(directory)
        else:
            print("Invalid arguments")
    except FileNotFoundError:
        print("Invalid filename or directory")

main()