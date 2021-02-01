import utilities.dice as Dice


class Engine:
    def __init__(self):
        pass

    def run_engine(self):
        """
        Runs the ttrpg engine, providing an interactive session to call common commands

        :return: None
        """
        while True:
            # Get user input
            user_input = input("command: ").lower()

            # Execute action
            if user_input == 'quit':
                break
            elif user_input == 'help':
                print("TODO: Add Help")
            elif user_input.startswith('roll'):
                roll_input = user_input.split(' ')
                if len(roll_input) != 2:
                    print("Invalid command - run 'roll xdy' where\n"
                          "x: the number of dice to roll\n"
                          "y: the number of sides on a single die")
                else:
                    roll_values = Dice.parse_dice_notation(roll_input[1])
                    if roll_values is not None:
                        print(Dice.roll_die(int(roll_values[0]), int(roll_values[1])))
            else:
                print("Unsupported command - try 'help'")
