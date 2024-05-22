def get_command_number(command):
    commands = {
            "сложение": 1,
            "вычитание": 2,
            "умножение": 5,
            "деление": 6,
            "запись": 7
        }
    return commands.get(command.lower())

def main():
    while True:
        command = input("Введите команду (сложение, вычитание, умножение, деление, запись): ").strip().lower()
        command_number = get_command_number(command)
        if command_number is None:
            print("Неверная команда. Попробуйте снова.")
            continue

        if command_number == 7:
            break

        try:
            num1 = int(input("Введите первое число: ").strip())
            num2 = int(input("Введите второе число: ").strip())
        except ValueError:
            print("Неверный ввод. Введите целые числа.")
            continue

        # Формируем содержимое файла
        output = ["v2.0 raw"]

        # Первая строка: номер команды и форматирование
        if command_number in {5, 6}:  # Для умножения и деления
            line1 = ["0", "10", f"{command_number}11", "0712", "12*0"]
        else:  # Для сложения и вычитания
            line1 = ["0", f"{command_number}10", f"{command_number}11", "0712", "12*0"]
        output.append(" ".join(line1))

        # Вторая строка: введенные числа и оставшиеся ячейки
        line2 = [str(num1), str(num2)]
        output.append(" ".join(line2))

        # Запись в файл
        with open("output", "w") as f:
            f.write("\n".join(output))

        print("Данные успешно записаны в output")
        break

if __name__ == "__main__":
    main()
