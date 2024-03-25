class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        response: str = input(prompt)
        return response


# Example usage:
if __name__ == "__main__":
    # Creating an instance of UserInputParser
    parser = UserInputParser()

    # Asking user for input using the parser
    username = parser.parse("Enter your username: ")
    print("Username entered:", username)

    password = parser.parse("Enter your password: ")
    print("Password entered:", password)

