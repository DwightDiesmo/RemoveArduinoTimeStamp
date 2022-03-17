import os

directoryPath = ''
directoryFiles = os.listdir(directoryPath)
print(directoryFiles)
for file in directoryFiles:
    filepath = file
    with open(directoryPath+filepath) as fp:
        line = fp.readline()
        f = open(directoryPath+"converted_"+filepath, "w")
        while line:
            length = len(line)
            position = 0;
            for char in line:
                if char == '>':
                    position += 2
                    break
                else:
                    position += 1
            converted = ""
            for x in range(position, length):
                converted += line[x]
            f.write(converted)
            line = fp.readline()
    f.close()