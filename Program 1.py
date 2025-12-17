# This program takes input for your name and return's its length.
# It also tells you what your age will be the next year.

print('Hello What is your name?')
name=input('>')
print('Hello ' + name)
name_length=len(name)
print('Your name length is : ')
print(name_length)
print('What is your age?')
age=input('>')
print('You will be ' + str(int(age)+ 1)  + ' next year')
 
 