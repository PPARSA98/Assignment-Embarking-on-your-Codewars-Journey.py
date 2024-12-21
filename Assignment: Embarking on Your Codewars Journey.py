# Challenge 1: Even or Odd
# Start by defining the numerical value of a predefined variable 
# For this project we will be using the variable 'x'
# Followed by the code that shows the labels the numerical value as "Even" or "Odd"

x = 0
if x % 2 == 0:
           print("Even")
else:
    print("Odd")
#Trying a new number    
y = 3
if y % 2 == 0:
        print("Even")  
else:
        print("Odd") 

# Challenge 2: Convert a Number to a string
# Convert a Number to a String. 
# Convert an number to a string using the str() function. 
# For example if you have,
a = 5
# And you want to convert it to a string
# first define the string as a variable, for example 'x'
x = str(5)
# This would output '5' . 
# Now print your string
print(x)    
# You can also do this by casting the integer as a string. 
# For example we will use the variable 'y'
y = '6'
# Now print your string
print(y)

# Challenge 3: Vowel Count  
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
# First, create a string to define the word you want a vowel count of.
string = "antidisestablishmentarianism"
# Then define the vowels being counted.
vowels = "aeiou"

# Next write a line of code to count the sum of the vowels.
count = sum(string.count(vowel) for vowel in vowels)
# Now print the vowel count.
print(count)      
# Try as many words as you would like. Even fake words. For example:
string_2 = "supercalifragilisticexpialidocious" 
# vowels is already defined as a string in the code.
count_2 = sum(string_2.count(vowel)for vowel in vowels)
print(count_2)      
