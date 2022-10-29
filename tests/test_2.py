import random

def againAndAgain():
    print('¿Cuantas preguntas quieres contestar?')
    numberOfProblems = input()
    numberOfProblems = int(numberOfProblems)

    if numberOfProblems < 0:
        print('Gracias por jugar,')
        exit()
    else:
        for problemsWanted in range(numberOfProblems):
            question1 = 1
            question2 = 2
            question3 = 3
            question4 = 4
            question5 = 5

            questionNumber = random.randint(1,5)

            if questionNumber == 1:
                question1Answer = input('¿Cual es la capital de Alemania? 1(Berlin), 2(Paris), 3(Roma) ')
                if question1Answer == '1':
                    print('Correcto')
                else:
                    print('Incorrecto')

            if questionNumber == 2:
                question2Answer = input('¿En qué año nació Napoleon Hill? 1(1886), 2(1898), 3(1883)? ')
                if question2Answer == '3':
                    print('Correcto')
                else:
                    print('Incorrecto')

            if questionNumber == 3:
                question3Answer = input('¿Cómo se llamó el plan para invadir a la URSS? 1(Plan Lebenraum) 2(Plan Barbarroja) 3(Plan Östlicher) ')
                if question3Answer == '2':
                    print('Correcto')
                else:
                    print('Incorrecto')

            if questionNumber == 4:
                question4Answer = input('¿Quién goberno durante el Tercer Imperio Mexicano? 1(Porfirio Diaz) 2(Maximiliano de Habsburgo) 3(Benito Juerez)? ')
                if question4Answer == '2':
                    print('Correcto')
                else:
                    print('Incorrecto')

            if questionNumber == 5:
                question5Answer = input('¿Cuándo fue el porfiriato? 1(1888 - 1912) 2(1871 - 1911) 3(1876 - 1911) ')
                if question5Answer == '3':
                    print('Correcto')
                else:
                    print('Incorrecto')

        print('Gracias por jugar')

againAndAgain()
