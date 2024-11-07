import json

institutions = [
    {
        "name": "School 1",
        "type": "school",
        "students": 450
    },
    {
        "name": "Technical College 1",
        "type": "college",
        "students": 300
    },
    {
        "name": "Vocational School 1",
        "type": "vocational",
        "students": 200
    },
    {
        "name": "School 2",
        "type": "school",
        "students": 500
    },
    {
        "name": "Technical College 2",
        "type": "college",
        "students": 350
    },
    {
        "name": "Vocational School 2",
        "type": "vocational",
        "students": 180
    }
]

jsonData = json.dumps(institutions)
with open("data.json", "wt") as file:
    file.write(jsonData)

def print_json():
    with open("data.json", "rt") as file:
        institutions = json.load(file)
        print(*institutions, sep='\n')

def add_del(operation, filename="data.json"):
    with open(filename, "rt") as file:
        data = json.load(file)

    if operation == "add":
        name = input("Введіть назву навчального закладу: ")
        type_ = input("Введіть тип закладу (school, college, vocational): ")
        students = int(input("Введіть кількість учнів: "))
        new_record = {"name": name, "type": type_, "students": students}
        data.append(new_record)
        print(f"Додано запис: {new_record}")
    elif operation == "delete":
        name = input("Введіть назву закладу, який потрібно видалити: ")
        data = [institution for institution in data if institution.get("name") != name]
        print(f"Запис із назвою '{name}' видалено (якщо існував)")
    else:
        print("Неправильна операція")
        return

    with open(filename, "wt") as file:
        json.dump(data, file)

def search_in_json(field, value, filename="data.json"):
    try:
        with open(filename, "rt") as file:
            data = json.load(file)

        results = [institution for institution in data if str(institution.get(field)) == str(value)]

        if results:
            print("Знайдені записи:")
            for result in results:
                print(result)
        else:
            print("Записи не знайдено за заданим критерієм.")

    except FileNotFoundError:
        print("Файл не знайдено.")
    except KeyError:
        print("Невірне поле для пошуку.")
    except json.JSONDecodeError:
        print("Помилка у форматі JSON файлу.")


def calculate_school_students(filename="data.json"):
    try:
        with open(filename, "rt") as file:
            data = json.load(file)

        total_students = sum(institution["students"] for institution in data if institution["type"] == "school")

        print(f"Загальна кількість учнів у школах: {total_students}")

        with open("data1.json", "wt") as output_file:
            json.dump({"total_school_students": total_students}, output_file)

        print("Інормація успішно записана до нового json-файлу")

    except FileNotFoundError:
        print("Файл не знайдено.")
    except json.JSONDecodeError:
        print("Помилка у форматі JSON файлу.")

while True:
    print(
        "Оберіть операцію: 1 - роздрукувати вміст, 2 - видалити/додати дані, 3 - пошук інформації, 4 – кількість учнів шкіл, 5 - вихід")
    t = int(input("Введіть номер:"))

    if t == 1:
        print_json()
    elif t == 2:
        operation = input("Введіть операцію (add/delete): ").strip()
        add_del(operation)
        print_json()
    elif t == 3:
        print("Введіть поле для пошуку (name, type, students): ")
        field = input().strip()
        print("Введіть значення для пошуку: ")
        value = input().strip()
        search_in_json(field, value)
    elif t == 4:
        calculate_school_students()
    elif t == 5:
        quit(0)






