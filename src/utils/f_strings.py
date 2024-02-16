import re
import logging


person = "John"
age = 23
print(f"Hi, my name is {person} and I am {age} years old.")

message = f"Hi, my name is {person} and I am {age} years old."
print(message)

message = "\n%s is %d years old"
print(message % (person, age))


def is_this_a_valid_email(email):
    if "@" not in email or "." not in email:
        return False

    at_index = email.index("@")
    dot_index = email.index(".")

    if at_index >= dot_index:
        return False

    if email.count("@") > 1 or email.count(".") > 1:
        return False

    if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
        return False

    return True


email = "email@email.com"
if is_this_a_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")


player = {'name': 'John', 'age': 23}
message = "\n{name} is {age} years old".format(**player)
print(message)


def longest_word(text):
    longest = "00"
    for word in text.split():
        if len(word) % 2 == 0 and len(word) > len(longest):
            longest = word
    return longest


strings = ["This is a test", "This is a test of the longest word function",
           "This is a test of the longest word function in the world"]

for string in strings:
    print(f"The longest word in '{string}' is '{longest_word(string)}'.")


def is_palindrome(text):
    text = re.sub(r"\W", "", text.lower())
    return text == text[::-1]


def caret_and_exponentiation():
    print(f"2^3 = {2**3}")  # exponentiation
    print(f"2^3 = {pow(2, 3)}")  # exponentiation
    print(f"2^3 = {2^3}")  # bitwise XOR


def never_using_comprehensions():
    dict_comp = {i: i*i for i in range(10)}
    list_comp = [x*x for x in range(10)]
    set_comp = {i % 3 for i in range(10)}
    gen_comp = (2*x+5 for x in range(10))


def always_using_comprehensions(a, b, n):
    c = []
    for i in range(n):
        for j in range(n):
            ij_entry = sum(a[n * i + k] * b[j + n * k] for k in range(n))
            c.append(ij_entry)
    return c


def checking_bool_or_len(x):
    if bool(x):
        pass

    if len(x) != 0:
        pass

    # The above two are equivalent to the following
    if x:
        pass


def print_vs_logging():
    print("This is a print statement.")
    logging.info("This is a logging statement.")
    logging.warning("This is a logging warning.")
    logging.error("This is a logging error.")
    logging.critical("This is a logging critical error.")


def bit_of_everything():
    level = logging.DEBUG
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)
    print_vs_logging()
    checking_bool_or_len("Hello")
    always_using_comprehensions([1, 2, 3, 4], [5, 6, 7, 8], 2)
    never_using_comprehensions()
    caret_and_exponentiation()
    is_palindrome


# for non library code best practice is to use the following
# if __name__ == "__main__":
#     main()
