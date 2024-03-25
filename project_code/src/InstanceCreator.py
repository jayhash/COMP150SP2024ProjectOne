# InstanceCreator.py
from project_code.src.User import User
from project_code.src.UserFactory import UserFactory
from project_code.src.UserInputParser import UserInputParser


class InstanceCreator:

    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
            return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self) -> User:
        # Placeholder for loading existing user data
        username = self.parser.parse("Enter your username:")
        # Assuming there's some method in UserFactory to load existing user data
        return self.user_factory.load_user(username)


# Example usage:
if __name__ == "__main__":
    from project_code.src.UserFactory import SimpleUserFactory
    from project_code.src.UserInputParser import SimpleUserInputParser

    # Creating instances of UserFactory and UserInputParser
    user_factory = SimpleUserFactory()
    parser = SimpleUserInputParser()

    # Creating an instance of InstanceCreator
    creator = InstanceCreator(user_factory, parser)

    # Example: Asking user if they want to create a new user or login
    response = "yes"  # Assuming user wants to create a new user
    user = creator.get_user_info(response)
    print(user.username)  # Assuming User class has a 'username' attribute
