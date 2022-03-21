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


def the_end(user_name):
    print(f"Congratulations, {user_name}!")
