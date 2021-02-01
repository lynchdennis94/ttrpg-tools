import random


def roll_die(number_of_dice, sides):
    """
    Rolls dice of the specified size, and returns a list of the roll outputs

    :param number_of_dice: an int defining the number of dice to roll
    :param sides: an int defining the number of sides on each die
    :return: a list of ints, with each element representing the result of a single die roll
    """
    result = []
    for roll in range(0, number_of_dice):
        result.append(random.randint(1, sides))

    return result


def parse_dice_notation(dice_input):
    """
    Parses out the standard dice notation xdy, where x is the number of dice to roll, and y is the number of sides on
    a single die

    :param dice_input: a string of the format xdy
    :return: a tuple (x,y) representing (number of dice, number of sides)
    """
    values = dice_input.split('d')
    if len(values) != 2:
        print("Invalid notation: please describe dice using xdy, where:\n"
              "x: the number of dice to roll\n"
              "y: the number of sides on each die")
        return None
    else:
        return values[0], values[1]
