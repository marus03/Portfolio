import random

def roll_dice(amount: int = 1) -> (list[int], int):
    if amount <= 0:
        raise ValueError
    sum: int = 0

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
        sum += random_roll


    return rolls, sum

def main():
    while True:
        try:
            user_input: str = input('Enter amount of rolls you wanna do: ')

            if user_input.lower() == 'exit':
                print('Thanks for playing, see you soon ;)')
                break

            rolls, rolls_sum = roll_dice(int(user_input))
            print('rolls:', ', '.join(map(str, rolls)), 'sum of rolled eyes:', rolls_sum)


        except ValueError:
            print('Please enter valid number between 1 to 6')

if __name__ == '__main__':
    main()