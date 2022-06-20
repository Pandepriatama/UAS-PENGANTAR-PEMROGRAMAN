data = []

while True:
    User = input("masukkan angka: ")
    if User == "n":
        break
    data.append(int(User))

total = sum(data)
rata = total/len(data)
print(rata)
