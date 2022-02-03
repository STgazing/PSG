#This program generates a random password
import random
import os
# colors
class color : 
   GREEN = '\033[92m'
   RED = '\033[91m'
   WHITE = '\033[0m'
   Blue = '\033[94m'
def stars():
    #This function specifies the number of stars
    if count < 16:
        print(color.GREEN + '*' * 16)
    else:
        print(color.GREEN + '*' * count) 

print(color.RED + '''
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
''')
print(color.Blue + '          Folow on Github: https://github.com/STgazing/PSG')
print(color.Blue + '                  Telegram: @mbin_gh or @Mhyar_nsi')
print('''
''')
count = int(input(color.WHITE +'[+] Please Enter The Number Of Password Digits: '))
print('''
''')
# Clear the terminal after sending the number
# Updated on February 3, 2021 
import os
os.system('clear')
# Sending the number
if count > 94 or count < 1:
    print('Unauthorized Number!')
else:
    passchars = list('''0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/''')
    random.shuffle(passchars)
    stars()
    print('[-] Your Password:')
    for i in passchars[:count]:
        print(i,end='')
    print('')    
    stars()    

print('''
''')
