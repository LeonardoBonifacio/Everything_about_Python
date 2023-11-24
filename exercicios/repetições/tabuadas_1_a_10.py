from os import system
system('cls')

print('Tabuadas de 1 a 10')
multi = 0 
num = 1
while(num != 11):
    if(multi == 11):
        num += 1
        multi = 0
    else:
        print(f'{num} x {multi} = {num * multi}')
        print()
        multi += 1
         