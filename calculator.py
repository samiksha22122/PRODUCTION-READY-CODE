# calculator.py

import logging
from abstraction import AbstractCalculator

# Setup logger
logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Info:
    def __init__(self):
        logging.info("This app is a command-line calculator supporting basic operations.")
        print("\n--- Python Calculator App ---")
        print("Supports: Addition, Subtraction, Multiplication, and Division")
        print("All operations are logged in 'calculator.log'.\n")


class Calculation(Info, AbstractCalculator):
    """
    Calculator class implementing basic arithmetic operations.
    Uses encapsulation to protect internal state and follows abstraction.
    """

    def __init__(self):
        super().__init__()
        self.__last_result = None  # Private variable

    def _add(self, num1, num2):
        result = num1 + num2
        self.__log_result("Add", num1, num2, result)
        self.__last_result = result
        return result

    def _subtract(self, num1, num2):
        result = num1 - num2
        self.__log_result("Subtract", num1, num2, result)
        self.__last_result = result
        return result

    def _multiply(self, num1, num2):
        result = num1 * num2
        self.__log_result("Multiply", num1, num2, result)
        self.__last_result = result
        return result

    def _divide(self, num1, num2):
        if num2 == 0:
            logging.error("Attempted division by zero")
            self.__last_result = None
            return "Error: Cannot divide by zero"
        result = num1 / num2
        self.__log_result("Divide", num1, num2, result)
        self.__last_result = result
        return result

    def __log_result(self, operation, num1, num2, result):
        logging.info(f"{operation}: {num1} and {num2} = {result}")

    def display_result(self):
        print(f"The result is: {self.__last_result}")
        logging.info(f"Displayed result: {self.__last_result}")


def main():
    logging.info("Calculator started")
    calc = Calculation()

    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            logging.info("Calculator exited by user")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                logging.info(f"Inputs received: num1={num1}, num2={num2}")

                if choice == '1':
                    result = calc._add(num1, num2)
                elif choice == '2':
                    result = calc._subtract(num1, num2)
                elif choice == '3':
                    result = calc._multiply(num1, num2)
                elif choice == '4':
                    result = calc._divide(num1, num2)

                # Only display result if it's not an error string
                if isinstance(result, str) and "Error" in result:
                    print(result)
                else:
                    calc.display_result()
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                logging.error("Invalid input: non-numeric value entered")
        else:
            print("Invalid choice. Please select again.")
            logging.warning("User entered an invalid choice")


if __name__ == "__main__":
    main()
