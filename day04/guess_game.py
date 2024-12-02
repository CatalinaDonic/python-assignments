from random import randrange

def guess_game(my_number, comp_number):
    if my_number < comp_number:
        return 'the number is bigger'
    elif my_number > comp_number:
        return 'the number is smaller'
    else:
        return 'you win!'

def main():
    while True:
        attempts = 0
        comp_number = randrange(1, 21)  # Range is 1 to 20 inclusive
        print('The computer chose a number between 1 and 20.')

        while True:
            my_input = input('Choose a number between 1 and 20 (x to exit, n for new game, s to show the number): ').strip()

            if my_input == 'x':
                print('Exiting the game, goodbye!')
                return  # Exit the program
            elif my_input == 'n':
                print('Starting a new game...')
                break  # Start a new game
            elif my_input == 's':
                print(f'The number is {comp_number}')
                continue  # Continue guessing the same number
            elif my_input.isdigit():
                my_number = int(my_input)
                attempts += 1
                result = guess_game(my_number, comp_number)
                print(result)
                if result == 'you win!':
                    print(f'You guessed the number in {attempts} attempts!')
                    play_again = input("Do you want to play again? (y/n): ").strip().lower()
                    if play_again != 'y':
                        print("Thanks for playing! Goodbye!")
                        return
                    else:
                        break  # Start a new game
            else:
                print('Invalid input. Please enter a number, x, n, or s.')

if __name__ == "__main__":
    main()
        



