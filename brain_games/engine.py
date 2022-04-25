import prompt


def run_game(get_description, get_question_answer):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}")

    print(get_description())

    game_round_count = 3
    for round_number in range(0, game_round_count):
        question, right_answer = get_question_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != right_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'\n"
                  f"Let's try again, {user_name}!")
            return

        print('Correct!')

    print(f"Congratulations, {user_name}!")
