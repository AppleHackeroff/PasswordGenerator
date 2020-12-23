import random
from pyautogui import alert
alert(title="Password Gen",text="Thanks for using is! Made By TheSpookyGames!")
uppercase_letters = "ABCDEFGHIJKLMNOPORSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "01234566789"
symbols = "()[]{},;:.- /\\?+*#= "

upper, lower, nums, sysm = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if sysm:
    all += symbols

length = 40
amount = 20

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)