#קלוט מהמשתמש את גובהו )עשרוני( , עד אשר יתקבל גובה בין 0.4 לבין 2.5
#בכל פעם שיתקבל גובה שלא בטווח הזה, הדפס : input wrong

#break = יציאה מהלולאה

while True:
    height = float(input("Enter height: "))
    if 0.4 <= height <= 2.5:
       print("Valid height")
       break
    else:
       print("Input wrong")

#קלוט מהמתשתמש 2 מספרים )שלמים (. והדפס את המספרים השלמים ביניהם.
#לדוגמא אם נקלט 1 ו- 5 ה דפס: 1 2 3 4 .5 שים לב: המספר הראשון שנקלט לא בהכרח
#קטן מהמספר השני שנקלט. כלומר אם נקלט 5 ו- ,1 אז יודפס: 5 4 3 2 1


num_1 = int(input('enter number:'))
num_2 = int(input('enter number:'))
if num_1 < num_2:
    for i in range(num_1 + num_2 +1):
        print(i)
else:
    for i in range(num_1 + num_2 -1, -1):
        print(i)



#ערכו של פאי )pie )הוא .3.14 שאל את המשתמש כמה שווה פאי? וקלוט את תשובתו
#בלולאה עד אשר יקליד את התשובה הנכונה. יש למשתמש 3 נסיונות בלבד .
#אם הצליח בתוך 3 נסיונות )או פחות(, הדפס: "correct are you"
#אם נכשל 3 פעמים צא מהלולאה והדפס: " 3.14 is pie "


pi = 3.14
counter = 3

for _ in range(counter):
    answer = float(input("What is the value of pi? "))
    if answer == pi:
       print("Correct!")
       break
else:
    print(f"pi_equal_3.14")



#קלוט מהמשתמש 3 מספרים בלולאה עד אשר :
#המספר הראשון שנקלט יהיה בין ,0-10
#+ וגם המספר השני שנקלט יהיה בין ,10-60
#+ וגם המספר השלישי שנקלט יהיה בין .60-100
#+ וגם המספר השני שנקלט יהיה ממוצע של שלושת המספרים.
#לדוגמא : 10 50 90
#קלוט בלולאה את 3 המספרים שוב ושוב ... עד אשר כל התנאים יתק יימו

while True:
    range1 = int(input("Enter a number between 0 and 10: "))
    range2 = int(input("Enter a number between 10 and 60: "))
    range3 = int(input("Enter a number between 60 and 100: "))

    if 0 <= range1 <= 10 and 10 <= range2 <= 60 and 60 <= range3 <= 100 and range2 == (range1 + range2 + range3) / 3:
        print("All conditions met!")
        break
    else:
        print("Conditions not met, try again.")








