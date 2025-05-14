import logging
from abstraction import AbstractConverter

# Setup logger
logging.basicConfig(
    filename='weight_converter.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Info:
    def __init__(self):
        logging.info("Weight Converter App Initialized")
        print("\n--- Python Weight Converter ---")
        print("Supports conversion between Kilograms and Pounds.\n")
        print("Note: K = Kilograms, L = Pounds\n")

class WeightConverter(Info, AbstractConverter):
    def __init__(self):
        super().__init__()
        self.__last_result = None

    def kg_to_lbs(self, weight):
        result = weight * 2.205
        self.__log("Kilograms to Pounds", weight, result)
        self.__last_result = round(result, 1)
        return self.__last_result

    def lbs_to_kg(self, weight):
        result = weight / 2.205
        self.__log("Pounds to Kilograms", weight, result)
        self.__last_result = round(result, 1)
        return self.__last_result

    def __log(self, operation, input_weight, result):
        logging.info(f"{operation}: {input_weight} -> {round(result, 1)}")

    def display_result(self, result, unit):
        print(f"Your weight is: {result} {unit}")
        logging.info(f"Displayed result: {result} {unit}")
