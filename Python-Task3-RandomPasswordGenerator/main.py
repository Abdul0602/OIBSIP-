import random
import string


def choose_character_sets():
    print("\nChoose character types to include:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Symbols")

    while True:
        choices = set(input("Enter at least 2 choices separated by spaces (example: 1 2 3): ").split())
        valid_choices = {"1", "2", "3", "4"}

        if not choices.issubset(valid_choices):
            print("Error: Please choose only 1, 2, 3, or 4.")
            continue
        if len(choices) < 2:
            print("Error: Please select at least 2 character types.")
            continue
        return choices


def generate_password(length, choices):
    character_sets = []
    required_characters = []

    if "1" in choices:
        characters = string.ascii_uppercase
        character_sets.append(characters)
        required_characters.append(random.choice(characters))
    if "2" in choices:
        characters = string.ascii_lowercase
        character_sets.append(characters)
        required_characters.append(random.choice(characters))
    if "3" in choices:
        characters = string.digits
        character_sets.append(characters)
        required_characters.append(random.choice(characters))
    if "4" in choices:
        characters = string.punctuation
        character_sets.append(characters)
        required_characters.append(random.choice(characters))

    all_characters = "".join(character_sets)
    remaining_length = length - len(required_characters)
    remaining_characters = [random.choice(all_characters) for _ in range(remaining_length)]

    password_characters = required_characters + remaining_characters
    random.shuffle(password_characters)
    return "".join(password_characters)


def get_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Error: Password length must be at least 8.")
                continue
            return length
        except ValueError:
            print("Error: Please enter a whole number.")


def main():
    print("=" * 35)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 35)

    while True:
        length = get_length()
        choices = choose_character_sets()
        password = generate_password(length, choices)

        print("\nGenerated password:")
        print(password)

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
