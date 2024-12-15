import random
import string

def main():
    text = ""
    palindromes = []
    algorithm_executed = False
    while True:
        print("Меню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            text = input_data()
            palindromes = []
            algorithm_executed = False
        elif choice == '2':
            if text:
                palindromes = find_palindromes(text)
                algorithm_executed = True
            else:
                print("Сначала введите данные.")
        elif choice == '3':
            if algorithm_executed:
                if palindromes:
                    print_palindromes(palindromes)
                else:
                    print("Палиндромы не найдены.")
            else:
                print("Сначала выполните алгоритм.")
        elif choice == '4':
            exit_program()
        else:
            print("Неверный выбор. Попробуйте снова.")

def input_data():
    print("Выберите способ ввода данных:")
    print("1. Ввести данные вручную")
    print("2. Сгенерировать данные случайным образом")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        text = input("Введите текст: ")
    elif choice == '2':
        text = generate_random_text()
    else:
        print("Неверный выбор. Попробуйте снова.")
        return input_data()

    return text

def generate_random_text():
    words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7))) for _ in range(20)]
    return ' '.join(words)

def find_palindromes(text):
    words = ''.join(char if char.isalnum() else ' ' for char in text).split()
    palindromes = [word for word in words if word == word[::-1]]
    return palindromes

def print_palindromes(palindromes):
    print("Найденные палиндромы:")
    for palindrome in palindromes:
        print(palindrome)

def exit_program():
    print("Программа завершена.")
    exit()

if __name__ == "__main__":
    main()
