from converter import WeightConverter
import logging

def main():
    logging.info("Application started")
    converter = WeightConverter()

    while True:
        try:
            weight = float(input("Enter your weight: "))
            unit = input("Kilograms or Pounds? (K or L, Q to quit): ").strip().upper()

            if unit == 'Q':
                print("Goodbye!")
                logging.info("Application exited by user")
                break

            if unit == 'K':
                result = converter.kg_to_lbs(weight)
                converter.display_result(result, "Lbs")
            elif unit == 'L':
                result = converter.lbs_to_kg(weight)
                converter.display_result(result, "Kgs")
            else:
                print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")
                logging.warning(f"Invalid unit entered: {unit}")

        except ValueError:
            print("Invalid input! Please enter numeric values for weight.")
            logging.error("Non-numeric weight entered")

if __name__ == "__main__":
    main()
