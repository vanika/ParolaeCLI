import os
from rich import print
from rich.console import Console
from rich.live import Live
from rich.table import Table
from ParolaeCLI.src.parolae import Parolae

ATTEMPTS = 6


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def main():
    parolae = Parolae()
    table = Table(title="Parolae", box=None)
    console = Console()

    remaining_attempts = ATTEMPTS
    status = False
    while remaining_attempts:
        guess = parolae.get_user_guess(remaining_attempts)
        status, result = parolae.try_word(guess)
        clear()
        with Live(table):
            msg = [f'[black on {color}] {letter} [/black on {color}]' for letter, color in result]
            table.add_row(*msg)
            table.add_row("")
        if status:
            remaining_attempts = 0
            print(console.print('\n :thumbs_up: Wow, you aced it!! \n'))
        else:
            remaining_attempts -= 1

    if not status:
        console.print(f'\n\n☹️  [bold red]Correct Word is {parolae.word_to_guess.upper()} [/bold red]')

if __name__ == '__main__':
    main()
