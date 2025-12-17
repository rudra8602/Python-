#This program uses while loops with flow control statements like break.
#the program asks for the username and password and loops itself until the condition is met.
print('Enter your Username.')
name=input('>')
while name != 'adam':
    print('Incorrect username,try again.')
    name=input('>')
    continue


while  True:
    
    print('Enter your password.')
    password=input('>')
    if password == 'reasonable':
     break
    
   


print('Access Granted')
    

