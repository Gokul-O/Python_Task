

# write a python program to calculate the total number of vowels and count of each individual
# vowel A,E,I,O,U



String = "Guvi Geeks Network Private Limited"
count = 0
String = String.upper()
for i in String:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count+=1
if count == 0:
    print('No vowels found')
else:
    print('Total no of vowels are :' + str(count))


# Input:"Guvi Geeks Network Private Limited"
# output:Total no of vowels are 12