letters=0
words=0
sentences=0
worddeviders=(","," ","-",":",";","'",'"',"/")
sentencedeviders=(".","?","!")
contents=" "
success=False

def getfilename():
    global success
    attempts=0
    while (not success) and (attempts<5):
        try:
            filename=input("Enter the text file examined, including its extension, e.g. filename.txt: ")
            datafile=open(filename,"r")
            success=True
        except IOError:
            print("Specified file cannot be found or opened.",end="")
            attempts=attempts+1
            if attempts<5:
                print(" Try again.")
            else:
                print()
            datafile=""
    return datafile

file=getfilename()
if not success:
    print("Too many attempts! Good-bye!")
else:
    while not contents=="":
        contents=file.readline()
        contents=contents.strip('\n')
        for k in range(0,len(contents)):
            if contents[k].isalnum():
                letters=letters+1
            elif (contents[k] in worddeviders) and (contents[k-1] not in sentencedeviders) and (contents[k-1] not in worddeviders):
                words=words+1
            elif (contents[k] in sentencedeviders) and (contents[k-1] not in sentencedeviders) and (contents[k-1] not in worddeviders):
                sentences=sentences+1
                words=words+1
            elif (contents[k] in sentencedeviders) and (contents[k-1] not in sentencedeviders) and (contents[k-1] in worddeviders):
                sentences=sentences+1
    print("Sentences: ",sentences,"\nWords: ",words,"\nLetters: ",letters)
    file.close()
