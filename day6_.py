class Password:
    def __init__(self, password: str):
        self._password = None
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value

    def check_strength(self):
        digits = "0123456789"
        special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

        has_digit = any(ch in digits for ch in self._password)
        has_special = any(ch in special_chars for ch in self._password)
        length = len(self._password)

        if length < 6:
            return "Weak"
        elif length >= 8 and has_digit and has_special:
            return "Strong"
        elif length >= 6 and has_digit:
            return "Medium"
        else:
            return "Weak"


# ---- User Input ----
password_objects = []

n = int(input("How many passwords do you want to check? "))

for i in range(n):
    user_password = input(f"Enter password {i + 1}: ")
    password_objects.append(Password(user_password))

# Display strength of each password
print("\nPassword Strength Results:")
for pwd in password_objects:
    print(f"{pwd.password} -> {pwd.check_strength()}")

# List comprehension to get strong passwords
strong_passwords = [
    pwd.password for pwd in password_objects
    if pwd.check_strength() == "Strong"
]

print("\nStrong Passwords:")
print(strong_passwords)
