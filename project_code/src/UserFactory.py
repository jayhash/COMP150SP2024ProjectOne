from project_code.src.UserInputParser import UserInputParser
from project_code.src.User import User

class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        # Here you can add more logic as needed, e.g., validate input
        return User(username, password)


# Example usage:
if __name__ == "__main__":
    from project_code.src.UserInputParser import SimpleUserInputParser

    # Creating an instance of UserInputParser
    parser = SimpleUserInputParser()

    # Creating a new user using UserFactory
    user = UserFactory.create_user(parser)
    print("New User Created:")
    print("Username:", user.username)
    print("Password:", user.password)

