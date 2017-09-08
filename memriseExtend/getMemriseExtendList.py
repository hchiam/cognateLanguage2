data1 = {}
data2 = {}

def txtToHashTable(fileName, dictionary):
    with open(fileName,'r') as f:
        for line in f:
            parts = line.split(',')
            key = parts[1] # English meaning
            val = parts[0] # generated word
            dictionary[key] = val

inputFile1 = 'cog1_output.txt' # '../' makes it look at the folder directory one above for that file
inputFile2 = '../output.txt' # '../' makes it look at the folder directory one above for that file
txtToHashTable(inputFile1, data1)
txtToHashTable(inputFile2, data2)

entries = []
for key in data2:
    if key in data1:
        entry = data1[key] + ' ' + data2[key] + '\t' + key
        entries.append(entry)

outputFile = 'for_memrise_extend.txt'
with open(outputFile,'a') as f:
    for entry in entries:
        f.write(entry + '\n')

import sortByEng
sortByEng.main(outputFile)
