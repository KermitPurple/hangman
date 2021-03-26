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
        for ch in self.word:
            if ch == ' ':
                print('   ', end='')
            elif ch in self.guesses:
                print(ch + ' ', end='')
            else:
                print('_ ', end='')
        print()

    def print_used_characters(self):
        for ch in 'abcefghijklmnopqrstuvwxyz':
            if ch in self.guesses:
                print(' ', end='')
            else:
                print(ch, end='')
        print()

    def get_input(self):
        print('Enter a key')
        while(1):
            ch = getch().decode('utf-8').lower()
            if ch in self.guesses:
                print('You already guessed that')
            elif ch.isalpha():
                self.guesses.add(ch)
                if ch not in self.word:
                    self.strikes += 1
                break

    def run(self):
        while(1):
            system('cls')
            print(self.frames[self.strikes])
            self.print_censored_word()
            self.print_used_characters()
            if(self.strikes == self.max_strikes - 1):
                print(f'The word was {self.word}!')
                break
            self.get_input()

if __name__ == '__main__':
    game = HangmanGame()
    game.run()

