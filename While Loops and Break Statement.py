#while loops
total = 0
for i in range(1,5):
    total += i
print(total)
total2 = 0
j = 1 #initialize j outside loop,
while j < 5: #helpeful when you don't know how many loops you need beforehand
    total2 += j
    j += 1
print(total2)

given_list = [5, 4, 4, 3, 1, -2, -3, -5] #don't know contents, just sorted in decending order
total3 = 0
i = 0
while given_list[i] > -2:
    total3 += given_list[i]
    i += 1
print(total3)
given_list2 = [5, 4, 4, 3, 1] #don't know contents, just sorted in decending order
total4 = 0
i = 0
while i < len(given_list2) and given_list2[i] > 0:
    total4 += given_list[i]
    i += 1
print(total4)
total5 = 0
given_list3 = [5, 4, 4, 3, 1, -2, -3, -4]
for e in given_list3:
    if e <= 0:
        break
         # this is a break statement

print(e)

total6 = 0
i = 0
while True:
    total6 += given_list3[i]
    i += 1
    if given_list3[i] <= 0:
        break
print(total6)
#challenge
given_list4 = [7, 5, 3, 2, 2, -1, -4, -7, -9]
i = len(given_list4) - 1
neg_total = 0
while i > 0 and given_list4[i] < 0:
    neg_total +=  given_list4[i]
    i -= 1
print(neg_total)




