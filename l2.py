string = input("Введите строку: ")
outstring = " "
n = 0

for i in range (0, len(string)):
    if i == 2:
        continue
    elif i == len(string) - 1:
        continue
    elif string[i] == "c" or string[i] == "с" \
            or string[i] == "C" or string[i] == "С":
        n += 1
    outstring += string[i]

if n >= 1:
    print("Присутствует символ 'c'!")

print("Строка со всеми изменениями: ", outstring)