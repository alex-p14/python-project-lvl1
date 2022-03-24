#!usr/bin/env python3
from random import randint, choice
from brain_games.general_logic import check_user_answer
from brain_games.general_logic import ask_question
from brain_games.general_logic import welcome_user
from brain_games.general_logic import finish_the_game


def find_expression_result(num_1, num_2, operator):
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    else:
        result = num_1 * num_2
    return str(result)


def begin_brain_calc(user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        finish_the_game(user_name)
    else:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        operator = choice('+-*')
        question = f"{num_1} {operator} {num_2}"
        user_answer = ask_question(question)
        right_answer = find_expression_result(num_1, num_2, operator)
        if check_user_answer(user_answer, right_answer, user_name):
            num_of_repeat += 1
            return begin_brain_calc(user_name, num_of_repeat)


def main():
    user_name = welcome_user()
    print('What is the result of the expression?')
    begin_brain_calc(user_name)


if __name__ == 'main':
    main()
