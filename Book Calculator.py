import math

#typecasting is converting a string to an int
name = input("Enter book name: ")
pages = int(input("Enter number of pages:"))
words = int(input("Enter number of words on one page: "))
hh_finish = round((pages*words/270/60)*2)

print("You will finish this book in "  + str(hh_finish)+  " days!")
file1 = open(r"C:\Users\drewb\Desktop/BookList.txt","a")
file1.write(name)
file1.write( "\n"+str(hh_finish) + " days to finish")
#12 rules for life 210 pages 385wpp

