import os
filePath = "a/v/123.txt"
if not os.path.exists(filePath):
    with open(filePath,'wb') as f :
        f.write("1232")