str="Python is a object oriented language"
cnt=0
for i in str:
    if i.isspace():
        cnt+=1
print("Total number of words in string is",cnt)