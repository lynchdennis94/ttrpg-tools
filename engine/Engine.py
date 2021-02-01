class Engine:
    def __init__(self):
        pass

    def run_engine(self):
        while True:
            # Get user input
            user_input = input("command: ")

            # Execute action
            if user_input == 'quit':
                break
            elif user_input == 'help':
                print("TODO: Add Help")
            else:
                print("Unsupported command - try 'help'")
