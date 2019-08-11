import math

#typecasting is converting a string to an int
pages = int(input("Enter number of pages:"))
words = int(input("Enter number of words on one page: "))
hh_finish = round((pages*words/270/60)*2)
print(f"You will finish this book in {hh_finish} days!")
#add excel function (or google sheets function?)

