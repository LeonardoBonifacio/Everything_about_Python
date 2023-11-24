from os import system
from phone import Phone
from keyboard import Keyboard
system('cls')

item1 = Keyboard("jscPhone",1000,3)

item1.apply_discount()

print(item1.price)