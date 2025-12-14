import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters   # A-Z, a-z
    if use_digits:
        character_pool += string.digits          # 0-9
    if use_symbols:
        character_pool += "!@#$%^&*()_+-=<>?/"

    if not character_pool:
        print("Error: No character set selected!")
        return ""

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password


print("=== Random Password Generator ===")

try:
    length = int(input("Enter password length: "))

    print("Include letters? (y/n): ", end="")
    use_letters = input().lower() == "y"

    print("Include digits? (y/n): ", end="")
    use_digits = input().lower() == "y"

    print("Include symbols? (y/n): ", end="")
    use_symbols = input().lower() == "y"

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print("\nGenerated Password:", password)

except ValueError:
    print("Error: Enter a valid number for length!")