#!usr/bin/env python3
from random import randint
from brain_games.general_logic import (
    check_user_answer,
    ask_question,
    welcome_user,
    finish_the_game
)


def get_next_num(amount_nums, next_num, step, hid_num, counter=1, squence=''):
    if amount_nums < counter:
        return squence
    elif hid_num == counter:
        squence += " .."
    else:
        squence += f" {next_num}"
    counter += 1
    next_num += step
    return get_next_num(amount_nums, next_num, step, hid_num, counter, squence)


def find_hidden_num(first_num, step_size, hidden_element):
    return str(first_num + step_size * (hidden_element - 1))


def get_number_squence():
    amount_nums = randint(6, 10)
    first_num = randint(1, 100)
    step = randint(2, 9)
    hidden_element = randint(2, amount_nums)
    num_squence = get_next_num(amount_nums, first_num, step, hidden_element)
    hidden_number = find_hidden_num(first_num, step, hidden_element)
    return (num_squence, hidden_number)


def begin_brain_progression(user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        finish_the_game(user_name)
    else:
        (question, right_answer) = get_number_squence()
        user_answer = ask_question(question)
        if check_user_answer(user_answer, right_answer, user_name):
            num_of_repeat += 1
            return begin_brain_progression(user_name, num_of_repeat)


def main():
    user_name = welcome_user()
    print("What number is missing in the progression?")
    begin_brain_progression(user_name)


if __name__ == 'main':
    main()
