#!/usr/bin/env python3
from random import randint
import prompt


def check_of_even_num(number):
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def is_even_num(user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        print(f"Congratulations, {user_name}!")
    else:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        random_num = randint(1, 100)
        print(f"Quation: {random_num}")
        your_answer = prompt.string("Your answer: ")
        right_answer = check_of_even_num(random_num)
        if right_answer == your_answer:
            print("Correct!")
            num_of_repeat += 1
            return is_even_num(user_name, num_of_repeat)
        else:
            print(f"'{your_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'\n"
                  f"Let's try again, {user_name}!")


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    is_even_num(name)


def main():
    welcome_user()


if __name__ == '__main__':
    main()
