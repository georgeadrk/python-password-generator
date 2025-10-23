import secrets
import string

class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # Get characters from string module
        self.base_characters: str = string.ascii_lowercase + string.digits
        self.uppercase_characters: str = string.ascii_uppercase
        self.symbols: str = string.punctuation

        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)

def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=False)

    for i in range(10):
        generated: str = password.generate()
        print(f'{generated} ({len(generated)} chars)')

if __name__ == '__main__':
    main()