number = 6
if number < 10:
    print("less then 10")
else:
    print("more then 10")

number1 = int(input("enter your number: "))
if number1 == 15:
    print("equal to 15")
else:
    print("not equal to 15")
    
word = input("enter your word: ")
if word == "group84":
    print("you are correct")
else:
    print("you are wrong")

for a in range(50, 101 , 5):
    print(a)

for i in range(1):
    print("zuka kakhniashvili")

number2 = 20
while number2 <= 50:
    print(number2)
    number2 += 1

number3 = 0
for i in range(0 , 100):
    print(i)

while number3 < 100:
    print(number3)
    number3 += 1

for i in range(0 , 101):
    print(i)

while number3 <= 100:
    print(number3)
    number3 += 1

number4 = 10

for i in range(10, 21):
    print(i)

while number4 <= 20:
    print(number4)
    number4 += 1


    number5 = 100
    for i in range(100 , 200 , 5):
        print(i)

        while number5 <= 200:
            print(number5)
            number5 += 5

number6 = 10
for i in range(10 , -1 , -1):
    print(i)

while number6 >= 0:
    print(number6)
    number6 -= 1

number7 = float(input("enter number: "))

if number7 > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif number7 < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")

age = int(input("enter your age: "))

if age < 0:
    print("არასწორი ინფო")
elif age <= 12:
    print("ბავშვი ხარ")
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
    print("ზრდასრული ხართ")
elif age <= 120:
    print("ხანში შესული ხართ")
else:
    print("გურუ ან ჯადოქარი")

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
num3 = float(input("შეიყვანეთ მესამე რიცხვი: "))

largest = num1 

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3
print("უდიდესი რიცხვია:", largest)


day = int(input("enter number 1 to 7: "))

if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")

    number8 = float(input("enter number: "))

if number8 > 50:
    print(number8 * 5)
else:
    print(number8 ** 2)

password = input("enter password: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")


number9 = int(input("enter number: "))

i = 1
total = 0

while i <= number9:
    total += i
    i += 1

print("ჯამი არის:", total)




