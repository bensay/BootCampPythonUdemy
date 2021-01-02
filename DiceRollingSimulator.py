import random


def SimulateDice():
    return random.randint(1, 6)


def PrintDiceFace(number):
    if number == 1:
        print('---------')
        print('|       |')
        print('|   0   |')
        print('|       |')
        print('---------')
    elif number == 2:
        print('---------')
        print('|       |')
        print('| 0   0 |')
        print('|       |')
        print('---------')
    elif number == 3:
        print('---------')
        print('|   0   |')
        print('|   0   |')
        print('|   0   |')
        print('---------')
    elif number == 4:
        print('---------')
        print('| 0   0 |')
        print('|       |')
        print('| 0   0 |')
        print('---------')
    elif number == 5:
        print('---------')
        print('| 0   0 |')
        print('|   0   |')
        print('| 0   0 |')
        print('---------')
    elif number == 6:
        print('---------')
        print('| 0   0 |')
        print('| 0   0 |')
        print('| 0   0 |')
        print('---------')
    else:
        raise Exception('The dice Number {} should be an integer between 1 and 6'.format(number))


def Roll():
    PrintDiceFace(SimulateDice())


def Main():
    print('This is a Dice Simulator')
    activation = 'y'
    while activation == 'y':
        Roll()
        activation = input('Press "y" if you want to roll again.')


if __name__ == '__main__':
    Main()
