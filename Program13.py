#This program takes input from user and fits it into a list and print it out.
#You can also see whether a value you entered is there or not in list.
cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
      ' (Or enter q to stop.):')
    name = input('>')
    if name == 'q':
        break
    cat_names = cat_names + [name]  
print('The cat names are:')
for name in cat_names:
    print('  ' + name)
print('Enter a cat name to check it exist or not')
exist=input('>')
if exist not in cat_names:
    print('This cat name does not exist')
else:
    print('It exist')