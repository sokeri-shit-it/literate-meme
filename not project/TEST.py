A = []
B = ''
while True:
    B = input("Введите слово: ")
    if not B:
        break
    A.append(B)
for i in A:
    for j in range(len(i) // 2):
        if i[j] != i[len(i) - j + 1]:
            print(i)
        else:
            break
