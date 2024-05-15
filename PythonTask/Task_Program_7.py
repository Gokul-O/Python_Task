str = "Python is easy"
most_frequency = {}
for i in str:
   if i in most_frequency:
      most_frequency[i] += 1
   else:
      most_frequency[i] = 1
max_string= max(most_frequency, key = most_frequency.get)
print ("The maximum of all characters is : ",max_string)
