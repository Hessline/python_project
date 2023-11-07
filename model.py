import random
import string


def generate_random_password(length):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


class Model:
    login_data = []
    __master_password = ""

    def __init__(self, master_password):
        self.set_master_password(master_password)

    def set_master_password(self, master_password):
        self.master_password = master_password

    def add_password_details(self, website, username, password):
        self.login_data.append({"Website": website, "Username": username, "Password": password})

    def delete_password_details(self, website):
        for login in self.login_data:
            if login["Website"] == website:
                self.login_data.remove(login)
        return f"Password for website {website} was deleted successfully"

    def get_passwords(self, master_password):
        if self.master_password == master_password:
            if not self.login_data:
                return "You have not added any passwords yet, please add one"
            else:
                return self.login_data
        else:
            return "You entered the wrong password, please try again"


if __name__ == '__main__':
    model = Model("12245e345")
    print(generate_random_password(20))
    model.add_password_details("www.google.com", "glisic.teodor@gmail.com", generate_random_password(20))
    print(model.get_passwords("12245e345"))
    model.delete_password_details("www.google.com")
    print(model.get_passwords("12245e345"))
