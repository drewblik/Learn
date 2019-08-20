a = ["apple", "bananna", "republic"]
#for element in a:
#    print(element)
for i in range(len(a)): # 0 1 2
    for j in range(i + 1):
        print(a[i])
        #i = 0 -> j = 0
        #i = 1 - j = 0, 1
        # i = 2 - j = 0, 1, 2

