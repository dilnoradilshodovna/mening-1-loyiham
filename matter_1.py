
with open("numbers.txt", "r") as file:
    num = file.read().split()

text = ''.join([chr(int(char)) for char in num])

with open("text.txt", "w") as file:
    file.write(text)

print("Raqamlar ortidegi gap text.txt fayliga yozildi.")




