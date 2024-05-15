str="Gokul"
vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
new_str=""
for i in str:
    if i not in vowels:
        new_str=new_str+i
print("After removing the vowels in string",new_str)


# Input="Gokul"
# Output=Gkl