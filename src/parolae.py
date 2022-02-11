import random

from typing import List, Set
from rich.prompt import Prompt
from rich import print
from utils import CharacterMatch


def get_default_dictionary() -> Set[str]:
    with open("../word_dictionary.txt", "r") as file_words_dict:
        words_dict = set()
        for line in file_words_dict:
            words_dict.add(line.strip())
        return words_dict



GAME_WORD_SIZE = 5


class Parolae:

    def __init__(self, words_dictionary=None):
        if words_dictionary is None:
            words_dictionary = get_default_dictionary()
        self.words_dictionary = words_dictionary
        self.words_list = list(self.words_dictionary)
        self.word_to_guess = random.choice(self.words_list)
        self.game_word_size = GAME_WORD_SIZE
        self.user_guess = ""

    def try_word(self, guess: str) -> (bool, List[tuple]):

        guess.lower()

        if guess not in self.words_dictionary:
            raise Exception

        if len(guess) != self.game_word_size:
            raise Exception

        result = []
        perfect_match_counter = 0
        for ch_guess, ch_word in zip(guess, self.word_to_guess):
            if ch_guess == ch_word:

                result.append((ch_guess, CharacterMatch.PERFECT_MATCH.value))
                perfect_match_counter += 1
            elif ch_guess != ch_word and ch_guess in self.word_to_guess:
                result.append((ch_guess, CharacterMatch.EXIST_IN_STRING.value))
            else:
                result.append((ch_guess, CharacterMatch.NO_MATCH.value))

        return perfect_match_counter == GAME_WORD_SIZE, result

    def get_user_guess(self, remaining: int = None) -> str:
        self.user_guess = Prompt.ask(f"\n\n[gray]Guess your word ({remaining if remaining is not None else 0} guess left) [/gray]").strip()
        if len(self.user_guess) != self.game_word_size:
            print('\n [red]--- Wait a minute.... That ain\'t a five letter word !!!! --- \n')
            self.get_user_guess(remaining=remaining)
        elif self.user_guess not in self.words_dictionary:
            print('\n [red]--- Oops! Not a valid word!!!! --- \n')
            self.get_user_guess(remaining=remaining)

        return self.user_guess
