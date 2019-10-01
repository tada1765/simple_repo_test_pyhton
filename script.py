import sys

import requests

# name = input("Your name? ")
# print("Hello," , name)

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


result = "hi"
print(greet("World"))
print(greet("wq"))

# r = requests.get('https://coreyms.com')
# print(r.status_code)
