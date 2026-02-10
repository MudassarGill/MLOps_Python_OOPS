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
        print("3. forgot password")
        print("4. write a post...")
        print("5. Send message...")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.signup()
        elif choice == "3":
            self.forgot_password()
        elif choice == "4":
            self.write_post()
        elif choice == "5":
            self.send_message()
        elif choice == "6":
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
    def forgot_password(self):
        username = input("Enter your username: ")
        if username == self.username:
            self.password = input("Enter your new password: ")
            print("Password changed successfully")
            self.menu()
        else:
            print("Invalid username")
            self.menu()
    def write_post(self):
        if self.is_logged_in==True:
            post = input("Enter your post: ")
            print("Post written successfully")
            self.menu()
        else:
            print("Please login to write a post")
            self.menu()
    def send_message(self):
        if self.is_logged_in==True:
            message = input("Enter your message: ")
            receiver = input("Enter receiver username: ")
            print(f"Message sent to {receiver}")
            self.menu()
        else:
            print("Please login to send a message")
            self.menu()
        
obj = Chatbook()
obj.menu()      