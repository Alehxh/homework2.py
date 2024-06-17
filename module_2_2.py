first = input('Введите число ')
second = input('Введите 2-е число ')
thrid = input('Введите 3-е число ')
if first == second and thrid == second:
    print(3)
elif first == second or second == thrid or first == thrid:
    print(2)
else:
    print(0)
