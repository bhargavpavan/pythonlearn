file = open("sample1.txt","r")
count = 0
for line in file:
    words = line.split(" ")
    count+=len(words)
file.close()
print("number of words in file:",count)