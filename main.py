import csv


TODOS_FILE = "todos.csv"
todos = []


def add_one_task(title):
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    todos.append(title)


def print_list():
    if not todos:
        print("No tasks.")
        return

    for position, title in enumerate(todos, start=1):
        print(f"{position}. {title}")


def delete_task(number_to_delete):
    if number_to_delete < 1 or number_to_delete > len(todos):
        raise ValueError("That task number does not exist.")
    todos.pop(number_to_delete - 1)


def save_todos():
    with open(TODOS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows([title] for title in todos)


def load_todos():
    todos.clear()
    try:
        file = open(TODOS_FILE, "r", newline="", encoding="utf-8")
    except FileNotFoundError:
        return

    with file:
        for row in csv.reader(file):
            if not row:
                continue
            if len(row) != 1:
                raise ValueError("todos.csv must contain one task per row.")
            if row[0]:
                todos.append(row[0])


def main():
    load_todos()
    print("To-do list")

    while True:
        print("\n1. Add task\n2. Show tasks\n3. Delete task\n4. Save tasks\n5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            try:
                add_one_task(title)
            except ValueError as error:
                print(error)
            else:
                print("Task added.")
        elif choice == "2":
            print_list()
        elif choice == "3":
            try:
                number = int(input("Task number to delete: "))
                delete_task(number)
            except ValueError as error:
                print(error)
            else:
                print("Task deleted.")
        elif choice == "4":
            save_todos()
            print("Tasks saved.")
        elif choice == "5":
            save_todos()
            print("Tasks saved. Goodbye!")
            return
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
