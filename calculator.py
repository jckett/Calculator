"""
File:ChuKetterer_5.1.py
Name: Joi Chu-Ketterer
Date: 4/12/19
Course: DSC510 - Introduction to Programming
Desc: Program uses loops to perform arithmetic operations on user input
Usage: The user will decide if they want to perform basic arithmetic on two inputs, similar to a classic calculator, or determine the average of multiple numbers.
"""

#this defines how to operate + - * and / on any user input, and ensures only valid numbers are allowed
def performCalc(operation):

    abort = False

    print('\n' 'You can choose two numbers to perform', userChoice, 'on.')

    inputOne = input('    Enter first number: ')
    if len(inputOne) > 1:
        if inputOne[1] == '-':
            abort = True

    inputTwo = input('    Enter second number: ')
    if len(inputTwo) > 1:
        if inputTwo[1] == '-':
            abort = True

    if inputOne.lstrip('-').replace('.', '', 1).isdigit() and inputTwo.lstrip('-').replace('.', '', 1).isdigit() and abort == False:

        if(operation == 'addition'):
            print('    The answer is:', (float(inputOne) + float(inputTwo)))

        if(operation == 'subtraction'):
            print('    The answer is:', (float(inputOne) - float(inputTwo)))

        if(operation == 'multiplication'):
            print('    The answer is:', (float(inputOne) * float(inputTwo)))

        if(operation == 'division'):
            print('    The answer is:', (float(inputOne) / float(inputTwo)))

    else:
        print('\n' 'One of your numbers was invalid. Please try again.')
        performCalc(userChoice)

#this defines how to caluclate the average of an indefinite number of values, and only allows for valid numbers
def calcAverage():
    avg = False
    avg2 = False

    try:
        numList = int(input('\n' 'How many numbers would you like to find the average of? \n'))
        avg = True

    except ValueError:
        print('Please enter a valid number.')
        calcAverage()

    if avg == True:
        try:
            totalSum = 0
            for num in range(numList):
                numbers = float(input('    Please enter number: '))
                totalSum += numbers
                avg2 = True

        except ValueError:
            print('One of your numbers is invalid. Please try again.')
            avg2 = False
            calcAverage()

    if avg2 == True:

        avgNum = totalSum/numList
        print('    The average of your', (num + 1), 'numbers is:', '%.2f' % avgNum)

print("Welcome to Joi's Calculating Services")

while True:

    userChoice = input('\n' 'Which of the following services would you like to use today? \n'
                       '    addition \n'
                       '    subtraction \n'
                       '    multiplication \n'
                       '    division \n'
                       '    average \n'
                       "As a reminder, you may type 'end' to leave. \n"
                       )

    if userChoice == 'addition':
        performCalc(userChoice)
        continue

    if userChoice == 'subtraction':
        performCalc(userChoice)
        continue

    if userChoice == 'multiplication':
        performCalc(userChoice)
        continue

    if userChoice == 'division':
        performCalc(userChoice)
        continue

    if userChoice == 'average':
        calcAverage()
        continue

    if userChoice == 'end':
        print('\n' 'Goodbye!')
        break

    else:
        print('Please enter a valid option \n')
        continue
