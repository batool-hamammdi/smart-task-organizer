import json

tasks = []

def load_tasks():
    """Load tasks from file when program starts"""
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    """Save tasks automatically to file"""
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)



# CRUD operations

def add_task():
    title = input("أدخل عنوان المهمة: ")
    description = input("أدخل وصف المهمة: ")
    deadline = input("أدخل الموعد النهائي (YYYY-MM-DD): ")
    priority = input("أدخل الأولوية (High, Medium, Low): ")

    task = {
        "title": title,
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "status": "ToDo"
    }

    tasks.append(task)
    save_tasks()
    print("تمت إضافة المهمة بنجاح!")


def show_tasks(task_list=None):
    if task_list is None:
        task_list = tasks

    if not task_list:
        print("لا توجد مهام لعرضها.")
        return

    for i, task in enumerate(task_list, start=1):
        print(f"\nمهمة رقم {i}")
        print(f"العنوان: {task['title']}")
        print(f"الوصف: {task['description']}")
        print(f"الموعد النهائي: {task['deadline']}")
        print(f"الأولوية: {task['priority']}")
        print(f"الحالة: {task['status']}")


def edit_task():
    show_tasks()
    index = int(input("أدخل رقم المهمة للتعديل: ")) - 1

    if 0 <= index < len(tasks):
        tasks[index]["title"] = input("عنوان جديد: ")
        tasks[index]["description"] = input("وصف جديد: ")
        tasks[index]["deadline"] = input("موعد نهائي جديد: ")
        tasks[index]["priority"] = input("أولوية جديدة: ")
        save_tasks()
        print("تم تعديل المهمة بنجاح!")
    else:
        print("رقم غير صحيح!")


def delete_task():
    show_tasks()
    index = int(input("أدخل رقم المهمة للحذف: ")) - 1

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()
        print("تم حذف المهمة!")
    else:
        print("رقم غير صحيح!")


def mark_task_completed():
    show_tasks()
    index = int(input("أدخل رقم المهمة لتحديدها كمكتملة: ")) - 1

    if 0 <= index < len(tasks):
        tasks[index]["status"] = "Completed"
        save_tasks()
        print("تم تحديد المهمة كمكتملة!")
    else:
        print("رقم غير صحيح!")



# sorting

def sort_by_deadline():
    tasks.sort(key=lambda t: t["deadline"])
    print("تم الترتيب حسب الموعد النهائي.")


def sort_by_priority():
    order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda t: order.get(t["priority"], 4))
    print("تم الترتيب حسب الأولوية.")



# filtering

def show_completed_tasks():
    show_tasks([t for t in tasks if t["status"] == "Completed"])


def show_not_completed_tasks():
    show_tasks([t for t in tasks if t["status"] == "ToDo"])


def show_high_priority_tasks():
    show_tasks([t for t in tasks if t["priority"] == "High"])



# export

def export_tasks_to_text():
    with open("exported_tasks.txt", "w", encoding="utf-8") as file:
        for i, task in enumerate(tasks, start=1):
            file.write(f"Task {i}\n")
            for key, value in task.items():
                file.write(f"{key}: {value}\n")
            file.write("-" * 30 + "\n")
    print("تم تصدير المهام بنجاح!")



# menu

def menu():
    print("\n--- Smart Task Organizer ---")
    print("1. إضافة مهمة")
    print("2. عرض جميع المهام")
    print("3. تعديل مهمة")
    print("4. حذف مهمة")
    print("5. تحديد مهمة كمكتملة")
    print("6. ترتيب حسب الموعد النهائي")
    print("7. ترتيب حسب الأولوية")
    print("8. عرض المهام المكتملة")
    print("9. عرض المهام غير المكتملة")
    print("10. عرض المهام عالية الأولوية")
    print("11. تصدير المهام")
    print("12. حفظ وخروج")


def main():
    load_tasks()
    while True:
        menu()
        choice = input("اختر: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_task_completed()
        elif choice == "6":
            sort_by_deadline()
        elif choice == "7":
            sort_by_priority()
        elif choice == "8":
            show_completed_tasks()
        elif choice == "9":
            show_not_completed_tasks()
        elif choice == "10":
            show_high_priority_tasks()
        elif choice == "11":
            export_tasks_to_text()
        elif choice == "12":
            save_tasks()
            print("تم الحفظ، إلى اللقاء!")
            break
        else:
            print("خيار غير صحيح!")


if __name__ == "__main__":
    main()
