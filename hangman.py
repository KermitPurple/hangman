import random
from msvcrt import getch
from os import system


class HangmanGame:
    frames = [
r''' +------+
 |      |
 |      0
 |     /|\
 |      |
 |     / \
 |
-+-
''',
r''' +------+
 |      |
 |      0
 |     /|\
 |      |
 |     /
 |
-+-
''',
r''' +------+
 |      |
 |      0
 |     /|\
 |      |
 |
 |
-+-
''',
r''' +------+
 |      |
 |      0
 |     /|\
 |
 |
 |
-+-
''',
r''' +------+
 |      |
 |      0
 |     /|
 |
 |
 |
-+-
''',
r''' +------+
 |      |
 |      0
 |      |
 |
 |
 |
-+-
''',
r''' +------+
 |      |
 |      0
 |
 |
 |
 |
-+-
''',
r''' +------+
 |      |
 |
 |
 |  GAME OVER
 |
 |
-+-
''',
            ]

    def __init__(self):
        self.words = self.get_words()
        self.word = random.choice(self.words)
        self.strikes = 0
        self.max_strikes = len(self.frames)
        self.guesses = set()

    @staticmethod
    def get_words():
        with open('words.txt') as f:
            return [line[:-1] for line in f.readlines()]

    def print_censored_word(self):
        pass

    def print_used_characters(self):
        pass

    def run(self):
        while(self.strikes < self.max_strikes):
            system('cls')
            print(self.frames[self.strikes])
            self.print_censored_word()
            self.print_used_characters()

if __name__ == '__main__':
    game = HangmanGame()
    game.run()

