from logger import get_logger
from operators import Addition, Multiplication, Division


def input_complex_number(n):
    logger = get_logger("data_entry_functions")

    print(f"Введите {n} комплексное число")
    real = float(input("Введите действительную часть: "))
    imag = float(input("Введите мнимую часть: "))
    logger.info(f"Введено комплексное число: {complex(real, imag)}")
    return complex(real, imag)


def input_operation(math_action):
    logger = get_logger("data_entry_functions")
    if math_action == "+":
        logger.info(f"Введён оператор: {math_action}")
        return Addition()
    elif math_action == "*":
        logger.info(f"Введён оператор: {math_action}")
        return Multiplication()
    elif math_action == "/":
        logger.info(f"Введён оператор: {math_action}")
        return Division()
    else:
        logger.info(f"ОШИБОЧНО введён оператор: {math_action}")
        return input_operation(input("Неверное значение. Введите одну из операций:+,*,/"))