#This program generates a random password
import random
def stars():
    #This function specifies the number of stars
    if count < 16:
        print('*' * 16)
    else:
        print('*' * count) 

print('''
##################
PASSWORD GENERATOR
##################   

 ''')
count = int(input('Please Enter The Number Of Password Digits:  '))
print('''
''')
if count > 94 or count < 1:
    print('Unauthorized Number!')
else:
    passchars = list('''0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/''')
    random.shuffle(passchars)
    stars()
    print('Your Password Is:')
    for i in passchars[:count]:
        print(i,end='')
    print('')    
    stars()    

#Mobin Ghanbarpour
#Mahyar Nasiri
      
