import time

file = input('Please Input The file you want to clear dupe : ')
start = time.time()

openFile = open(file, "r")
writeFile = open("Cleaned.txt", "w")
tmp = set()
x = 0
for txtLine in openFile:
    if txtLine not in tmp:
        writeFile.write(txtLine)
        tmp.add(txtLine)
    else:
        x += 1

openFile.close()
writeFile.close()
end = time.time()
e = end - start
print(f'\nUsed {e} Seconds to Clear Dupes,Cleared {x} Lines')
