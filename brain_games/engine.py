import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def ask_question(question):
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    return answer


def check_user_answer(user_answer, right_answer, user_name):
    if user_answer == right_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{right_answer}'\n"
              f"Let's try again, {user_name}!")
        return False


def finish_the_game(user_name):
    print(f"Congratulations, {user_name}!")


def start_new_round(question_answer, user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        finish_the_game(user_name)
    else:
        question, rigth_answer = question_answer()
        user_answer = ask_question(question)
        if check_user_answer(user_answer, rigth_answer, user_name):
            num_of_repeat += 1
            return start_new_round(question_answer, user_name, num_of_repeat)


def run_game(get_description, get_question_answer):
    user_name = welcome_user()
    print(get_description())
    start_new_round(get_question_answer, user_name)
