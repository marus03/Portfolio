from random import choice

def run_game():
    word: str = choice(['orange', 'apple', 'watermelon'])

    username: str = input('What is your name? >> ')
    print(f'Welcome {username}!')

    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()

        if blanks == 0:
            print('You won!')
            break

        guess: str = input('Enter a letter: ')

        if len(guess) <= 1 and guess.isalpha() or guess == word:
            if guess in guessed:
                print(f'You already used: "{guess}". Please try with another letter.')
                continue

            guessed += guess

            if guess not in word:
                tries -= 1
                print(f'Sorry, wrong letter ({tries}) tries left')

                if tries == 0:
                    print('You lost :(')
                    break
        else:
            print('You have to enter only 1 letter!')

if __name__ == '__main__':
    run_game()