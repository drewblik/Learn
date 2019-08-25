d = {}
# d = {"George": 24, "Tom": 32}
d["George"] = 24
d["Tom"] = 32
print(d["George"])
d["Jenny"] = 20
print(d)
#keys are strings and numbers
d[10] = 100
print(d[10])
for key, value in d.items():
    print("Key:")
    print(key)
    print("Value:")
    print(value)
    print("")