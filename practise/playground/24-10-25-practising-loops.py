

for x in range(1,11): # x acts as a variable to store the current number being counted
    # it has to be in the range of 1-11 when counting to 10 as it's not inclusive
    print(x) # prints the variable that stores the current number being counted

print("") # just leaving a space

for y in reversed(range(1, 11)): # again y acts as a variable to store each number that being counted
    # the reversed part does what it says, it counts from 10 to 1 now
    print(y)
print("")

for z in range(2, 11, 2): # the extra 2 specifies its going up in the two times tables
    print(z)

word = input("Enter a word") # prompts the user to enter a word
#for a in word: # a is a variable that stores each letter in the word entered
#   print(a) # prints each letter seperately

#word2 = input("Enter a word") # this is another way of doing the same thing
#for b in range(len(word2)): # counts the length of the word b
#    print(word2[b]) # prints each letter seperately

for a in word:
    if a == "b":
        print("You cannot enter b")
        continue # this skips over any "b" when printing the word
       #break    # this would stop printing the word if it contains a "b"
    else:
        print(a)

