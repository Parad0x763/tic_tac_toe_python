from dataclasses import dataclass
from typing import Final

BLANK_SPACE: Final[str] = " "

@dataclass
class Game:
    board: list
    is_cross: bool

def set_up_initial_game() -> Game:
    return Game(
        board=[
            BLANK_SPACE, BLANK_SPACE, BLANK_SPACE,
            BLANK_SPACE, BLANK_SPACE, BLANK_SPACE,
            BLANK_SPACE, BLANK_SPACE, BLANK_SPACE
        ],
        is_cross=True,
    )

def action(game: Game, input: int) -> None:
    if game.board[input - 1] == BLANK_SPACE:
        game.board[input - 1] = "X" if game.is_cross else "O"

def has_won(game: Game) -> bool:
    if (
        # vertical wins
        (game.board[0] == game.board[1] and game.board[1] == game.board[2] and game.board[1] != " ") or
        (game.board[3] == game.board[4] and game.board[4] == game.board[5] and game.board[4] != " ") or
        (game.board[6] == game.board[7] and game.board[7] == game.board[8] and game.board[6] != " ") or
        # horizontal wins
        (game.board[0] == game.board[3] and game.board[3] == game.board[6] and game.board[3] != " ") or
        (game.board[1] == game.board[4] and game.board[4] == game.board[7] and game.board[4] != " ") or
        (game.board[2] == game.board[5] and game.board[5] == game.board[8] and game.board[5] != " ") or
        # diagonal wins
        (game.board[0] == game.board[4] and game.board[4] == game.board[8] and game.board[4] != " ") or
        (game.board[2] == game.board[4] and game.board[4] == game.board[6] and game.board[4] != " ")
    ):
        return True

    return False

def has_turns_ended(game: Game) -> bool:
    for tile in game.board:
        if tile == BLANK_SPACE:
            return False
    return True

def print_board(game: Game) -> None:
    print(f"""
| {game.board[0]} {game.board[1]} {game.board[2]} |
| {game.board[3]} {game.board[4]} {game.board[5]} |
| {game.board[6]} {game.board[7]} {game.board[8]} |
""")

def game_loop() -> None:
    game: Game = set_up_initial_game()
    while True:
        try:
            print("Enter 1-9 To play or 0 to end")

            user_input = int(input())

            if user_input == 0:
                break

            action(game, user_input)

            print_board(game)

            if has_won(game):
                win_text = "'X' player has won" if game.is_cross else "'O' player has won"
                print(f"Game over\n{win_text}")
                break

            if has_turns_ended(game):
                break

            game.is_cross = not game.is_cross

        except ValueError:
            print("Please enter a number between 1 and 9")
        except:
            print("An error occured. Game play is continuing.")
            continue

def main() -> None:
    game_loop()

if __name__ == "__main__":
    main()
