#print ("Hello, World!")

#print ("Hello, Git")

#name = "Michael"
#age = "36"
#print (name, age)

#num = int(input("Vvedite 4islo: "))
#if num % 3 == 0 and num % 5 == 0:
#    print("FizzBuzz")
#elif num % 3 == 0:
#    print("Fizz")
#elif num % 5 == 0:
#    print("Buzz")
#else: 
#    print(num)

#x = -25.5
#y = 5.7
#if x >= 0:
#    if y >= 0:  # x > 0, y > 0
#        print("Перша чверть")
#    else:  # x > 0, y < 0
#        print("Четверта чверть")
#else:
#    if y >= 0:  # x < 0, y > 0
#        print("Друга чверть")
#    else:  # x < 0, y < 0
#        print("Третя чверть")

# Зчитування рядка від користувача
#user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
#total_chars = len(user_input)  # загальна кількість символів у рядку
#space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
#for char in user_input:
#    if char == " ":
#        space_count += 1

# Виведення результатів
#print(f"Загальна кількість символів у рядку: {total_chars}")
#print(f"Кількість пробілів у рядку: {space_count}")


#age = input("How old are you? ")
#try:
#    age = int(age)
#    if age >= 18:
#        print("You are adult.")
#    else:
#        print("You are infant")
#except ValueError:
#    print(f"{age} is not a number")

days =  {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}
while True:
    i = input ('Enter a day, "q" for exit: ')
    try:
        value = int(i)
        print(days.get(value, "Такого дня немає"))
    except ValueError:
        if i == "q":
            break
        print("Потрібно ввести число")    