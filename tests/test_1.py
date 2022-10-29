import random

i = int(input("Write the number of attempts you want to try "))

x = 0

# while x < i:

#     print("To answer the questions, you must write 1, 2 or 3 to choose an answer, ¿Are you ready? (y)/(n)")
#     if input() == "y":
#         print("Let's star")

#     else:
#         print("Nice to meet you")
#         break

ans1 = "1"
ans2 = "2"
ans3 = "3"

if x < i:
    print("¿Alemania ganó la Segunda Guerra Mundial? 1(No) 2(Sí) 3(No sé)")
    if input() == ans1:
        print("you succeeded")
    else:
        print("you are wrong")
        x += 1

if x < i:
    print("¿Cómo se llamó el plan para invadir a la URSS? 1(Plan Lebenraum) 2(Plan Barbarroja) 3(Plan Östlicher) ")
    if input() == ans2:
        print("you succeeded")
    else:
        print("you are wrong")
        x += 1

if x < i:
    print("¿Cuándo terminó la SGM? 1(1944) 2(1950) 3(1945) ")
    if input() == ans3:
        print("you succeeded")
    else:
        print("you are wrong")
        x += 1

if x < i:
    print("¿En cuantas semanas cayó Francia? 1(4 semanas) 2(12 semanas) 3(20 semanas) ")
    if input() == ans1:
        print("you succeeded")
    else:
        print("you are wrong")
        x += 1

#x =+ 1

if x > i:
    print('Game Over')
    #break

#print(random.randint(q1, q2))

print("¡Good Game!")

if x == i:
    print("Your Mistakes", x)
else:
    print("Your don't have any mistakes")

#if x < i:
#     print("¿? 1() 2() 3() ")
#     if input() == ans:
#         print("you succeeded")
#     else:
#         print("you are wrong")
#         x =+ 1