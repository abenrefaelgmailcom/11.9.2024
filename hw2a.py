#.2 השתמש בלולאת for והדפס:
#- את כל המספרים השלמים מ- 0 ועד 10 כ ולל


x = int(input('enter number:'))
for i in range(0, 10 +1, +1):
   print(i, end=" ")
   print()


#- את כל המספרים הזוגיים מ 40- ועד 88 כולל


x = -40
for i in range(-40, 88 +2, +2):
    print(i, end=" ")
    print()


# את כל המספרים המתחלקים ב7- ) ללא שארית( מ77- ועד 105 כולל

x = -77
for i in range(-77, 105 +7, 7):
    print(i, end="")
    print()


#- את כל המספרים המתחלקים ב- 3 )ללא שארית( מ 99- ועד 66 )בסדר יורד(

x = -99
for i in range(-99, 66 +3, 3):
    print(i, end="")
    print()