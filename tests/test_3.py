#Number of trys
i = int(input("¿Cuantos intentos quieres intentar? "))

x = 0
#Variables of answers
ans1 = "1"
ans2 = "2"
ans3 = "3"

#Questions about of chemical

if x < i:
    print("¿Cuál es la principal función de los carbohidratos? 1(Dar más fuerza a los musculos) 2(Dar energia al cuerpo) 3(Dar grasa al cuerpo) ")
    if input() == ans2:
        print("Correcto")
    else:
        print("Incorrecto (2)")
        x += 1

if x < i:
    print("¿Cuál es su fórmula general de los carbohidratos? 1(CN (H2O)N) 2(CN (HO2)N) 3(CH (H20)N) ")
    if input() == ans1:
        print("Correcto")
    else:
        print("Incorrecto (1)")
        x += 1

if x < i:
    print("Es un derivado de un carbohidrato, formado por glucosa y galactosa 1(Lactosa) 2(Glucosa) 3(Fructuosa) ")
    if input() == ans1:
        print("Correcto")
    else:
        print("Incorrecto (1)")
        x += 1

if x < i:
    print("También conocido como... 1(Glucosa) 2(Sal) 3(Azúcares) ")
    if input() == ans1:
        print("Correcto")
    else:
        print("Incorrecto (3)")
        x += 1

if x < i:
    print("¿Cuál es su compuesto más importante de los carbohidratos? 1(La Fructuosa) 2(La glucosa) 3(La galactosa) ")
    if input() == ans2:
        print("Correcto")
    else:
        print("Incorrecto (2)")
        x += 1

# if x < i:
#     print(" 1() 2() 3() ")
#     if input() == ans:
#         print("Correcto")
#     else:
#         print("Incorrecto ()")
#         x += 1

#End of questions and start the final part

if x > i:
    print('Fin del juego')

print("¡Buen juego!")

#Number of mistakes of the Usuary

if x == i:
    print(f'Tu número de errores cometidos {x}')
else:
    print("No cometiste errores, felicidades")
