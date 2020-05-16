class User():

    def __init__(self, name, last_name , email_address, contact_number):
        self.name = name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_number = contact_number

    def describe_user(self):
        print("\n")
        print(f" name: {self.name}")
        print(f" last: {self.last_name}.")
        print(f" contact_number: {self.contact_number}")
        print(f" email address: {self.email_address}")


    def greet_user(self):
        print(f"\n Hello {self.name}")

louise = User('Louise' , 'Schaadra', 'LouiseS@gmail.com', '0827345981')
louise.describe_user()
louise.greet_user()

eric = User('Eric', 'Ustra' ,'EricU@gmail.com', '0834545789')
eric.describe_user()
eric.greet_user()
