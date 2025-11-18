students = {}

while True:
    name = input("Ім'я (stop - завершити): ")
    if name.lower() == "stop":
        break
    grade = input("Оцінка (1-12): ")
    if grade.isdigit() and 1 <= int(grade) <= 12:
        students[name] = int(grade)

print("\nУчні:")
for n, g in students.items():
    print(n, "-", g)

grades = students.values()
avg = sum(grades) / len(grades) if grades else 0
print("Середній бал:", round(avg, 2))

excellent = [n for n, g in students.items() if 10 <= g <= 12]
good = sum(1 for g in grades if 7 <= g <= 9)
weak = sum(1 for g in grades if 4 <= g <= 6)
bad = sum(1 for g in grades if 1 <= g <= 3)

print("Відмінники:", len(excellent), excellent)
print("Хорошисти:", good)
print("Відстаючі:", weak)
print("Не здали:", bad)