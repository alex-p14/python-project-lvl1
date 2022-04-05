#!usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.gcd import (
    get_description,
    get_question_and_answer
)


def main():
    run_game(get_description, get_question_and_answer)


if __name__ == 'main':
    main()
