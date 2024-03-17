import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to RPS')

        self.moves: dict = {'rock': '🗿', 'paper': '🧻', 'scissors': '🔪' }
        self.valid_moves: list[str] = list(self.moves.keys())
        self.points_p: int = 0
        self.points_ai: int = 0

    def play_game(self):
        user_move: str = input('Enter your choice >> ').lower()

        if user_move == 'exit':
            print('Thanks for playing. See you soon! :)')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move!')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)
        print(f'You: {self.points_p}')
        print(f'AI: {self.points_ai}')

    def display_moves(self, user_move: str, ai_move: str):
        print('------')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('------')

    def check_move(self, user_move: str, ai_move: str):

        if user_move == ai_move:
            print('It\'s a tie')
        elif user_move == 'rock' and ai_move == 'scissors':
            self.points_p += 1
            print('You won')
        elif user_move == 'scissors' and ai_move == 'paper':
            self.points_p += 1
            print('You won')
        elif user_move == 'paper' and ai_move == 'rock':
            self.points_p += 1
            print('You won')
        else:
            self.points_ai += 1
            print('You lost :(')




if __name__ == '__main__':
    rps = RPS()

    while rps.points_p < 3 and rps.points_ai < 3:
        rps.play_game()

    if rps.points_p == 3:
        print("Congratulations! You won the game!")
    else:
        print("You lost the game. Better luck next time!")
