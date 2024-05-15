str="Hackerrank"
count=0
new_str=[]

for i in str:
    if i not in new_str:
        count+=1
        new_str.append(i)
print("Total no of unique characters count is",count)

# Input="Hackerrank"
# Output=Total no of unique characters count is 7