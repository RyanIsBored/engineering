from random import randint
color = input('pick a color: red, blue, green, or yellow: ')


if color=='red':
    fortune=randint(0,3)

if color=='blue':
    fortune=randint(4,7)

if color=='green':
    fortune=randint(8,11)

if color=='yellow':
    fortune=randint(12,15)

if fortune==0:
    print("You will be hit by a car")
if fortune==1:
    print("You will win the lottery")
if fortune==2:
    print("You will have a nice week")
if fortune==3:
    print("You will have no homework for the rest of the week")
if fortune==4:
    print("You will step on a lego")
if fortune==5:
    print("You will find something you once lost")
if fortune==6:
    print("You will fly an airplane")
if fortune==7:
    print("You will win the Superbowl")
if fortune==8:
    print("You will get a papercut")
if fortune==9:
    print("Nothing will happen")
if fortune==10:
    print("You will hear your favorite song on the radio")
if fortune==11:
    print("You will eat at your favorite restaurant")
if fortune==12:
    print("Your favorite TV show will be canceled")
if fortune==13:
    print("You will explode")
if fortune==14:
    print("You will go on vacation")
if fortune==15:
    print("You will become famous")
