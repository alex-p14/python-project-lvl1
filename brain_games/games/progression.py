import random


def get_description():
    return 'What number is missing in the progression?.'


def get_next_num(amount_nums, next_num, step, hid_num, counter=1, squence=''):
    if amount_nums < counter:
        return squence
    elif hid_num == counter:
        squence += " .."
    else:
        if counter > 1:
            squence += " "
        squence += f"{next_num}"
    counter += 1
    next_num += step
    return get_next_num(amount_nums, next_num, step, hid_num, counter, squence)


def find_hidden_num(first_num, step_size, hidden_element):
    return str(first_num + step_size * (hidden_element - 1))


def get_number_squence():
    amount_nums = random.randint(6, 10)
    first_num = random.randint(1, 100)
    step = random.randint(2, 9)
    hidden_element = random.randint(2, amount_nums)
    num_squence = get_next_num(amount_nums, first_num, step, hidden_element)
    hidden_number = find_hidden_num(first_num, step, hidden_element)
    return num_squence, hidden_number


def get_question_and_answer():
    question, answer = get_number_squence()
    return question, answer
