#we want to make a login page same as facebook
class Chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.is_logged_in = False
    def menu(self):
        print("Welcome to Chatbook")
        print("1. Login")
        print("2. signup")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.signup()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice")
            self.menu()
    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print("Signup successful")
        self.menu()
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == self.username and password == self.password:
            print("Login successful")
            self.is_logged_in = True
            self.menu()
        else:
            print("Invalid username or password")
            self.menu()
        
obj = Chatbook()
obj.menu()      