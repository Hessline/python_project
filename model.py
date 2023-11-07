import random
import string


def generate_random_password(length):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


class Model:
    login_data = []

    def add_password_details(self, website, username, password):
        self.login_data.append({"Website": website, "Username": username, "Password": password})

    def delete_password_details(self, index):
        self.login_data.pop(index)
