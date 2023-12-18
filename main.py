from data_entry_functions import input_complex_number, input_operation
from logger import setup_logger, get_logger
from calculate import ComplexCalculator


def main():
    setup_logger()
    logger = get_logger("main")

    logger.info("Калькулятор комплексных чисел запущен.")

    logger.info("Ввод первого комплексного числа:")
    num1 = input_complex_number(1)

    logger.info("Ввод операции:+,*,/")
    operation = input_operation(input("Введите одну из операций:+,*,/"))

    logger.info("Ввод второго комплексного числа:")
    num2 = input_complex_number(2)

    calculator = ComplexCalculator(operation)

    result = calculator.calculate(num1, num2)
    logger.info(f"Вывод результата: {result}")

    print(f"Результат {calculator}: {result}")


if __name__ == "__main__":
    main()