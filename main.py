# 1-misol
yil = int(input("Yil kiriting: "))

if (yil % 4 == 0 and yil % 100 != 0) or yil % 400 == 0:
    print("Kabisa yili")
else:
    print("Oddiy yil")

# 2-misol
a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))

print("Eng kichik son:", min(a, b, c))

# 3-misol
raqam = int(input("Raqam kiriting (0 yoki 1): "))

if raqam == 0:
    print("0")
elif raqam == 1:
    print("1")
else:
    print("Boshqa raqam")

# 4-misol
a = int(input("To'rtburchakning 1-tomoni: "))
b = int(input("To'rtburchakning 2-tomoni: "))

if a == b:
    print("Kvadrat")
else:
    print("To'rtburchak")

#5-misol
son = int(input("Son kiriting: "))

if son <= 100:
    print("Kichik yoki teng 100")
else:
    print("Katta")

# 6-misol
a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))

print("Eng kichik son:", min(a, b, c))


