def generate_password(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i != j and (i + j) % n == 0:
                pairs.append((i, j))
    password = ''.join(f'{i}{j}' for i, j in pairs)
    return password
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Введите число от 3 до 20: "))
            if 3 <= n <= 20:
                print(f'Сгенерированный пароль: {generate_password(n)}')
                break
            else:
                print("Число должно быть в диапазоне от 3 до 20. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")