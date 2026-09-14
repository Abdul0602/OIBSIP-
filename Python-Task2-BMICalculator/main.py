def calculate_bmi(weight, height):
    """Calculate BMI using kilograms and meters."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Return the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_positive_number(prompt):
    """Read a positive number from the user with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a value greater than 0.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")


def main():
    print("=" * 30)
    print("        BMI CALCULATOR")
    print("=" * 30)

    weight = get_positive_number("Enter your weight (kg): ")
    height = get_positive_number("Enter your height (m): ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("\n--- Result ---")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
