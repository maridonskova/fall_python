import os


def file_numerator(path):
    def handle(string):
        index = string.rfind('/')
        return string[index+1::] if index >= 0 else string

    def recursive(path, massiv):
        array = os.listdir(path)
        for item in array:
            current = os.path.join(path, item)
            if os.path.isfile(current):
                massiv.append(handle(current))
            elif os.path.isdir(current):
                recursive(current, massiv)
    array = []
    recursive(path, array)
    for i in range(len(array)):
        print(str(i+1) + '. ' + array[i])
