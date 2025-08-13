tasks = [ ]

def menu():
    print("\n==============================")
    print("          TO-DO LIST          ")
    print("==============================")
    print("1) Add task")
    print("2) View tasks")
    print("3) Mark task as done")
    print("4) Delete task")
    print("5) Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!👋")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            
        input("\n(Press Enter to return to the menu)")


def add_task(tasks):
    title = input("\nEnter task title: ").strip()
    if not title:
        print("⚠️ Task title cannot be empty. Please try again.")
        return
    tasks.append({"title": title, "done": False })
    print(f"\n✅ Task added: {title}")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks added yet. Add one!")
        return
    print("\nYour tasks: ")
    for i, t in enumerate(tasks, start=1):
        box = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {box} {t['title']}")
     
def mark_done(tasks):
    if len(tasks) == 0:
        print("\n No tasks to mark. Add one first!")
        return
    view_tasks(tasks)
    
    num = input("\nEnter the task number to mark as done: ").strip()
    if not num.isdigit():
        print("⚠️ Please enter a valid number.")
        return
    
    index = int(num) - 1
    if index < 0 or index >= len(tasks):
        print("\n⚠️ That number is not in the list.")
        return
    
    if tasks[index]["done"]:
        print(f'\nℹ️ "{tasks[index]["title"]}" is already marked as done.')
    else:
        tasks[index]["done"] = True
        print(f'\n✅ Marked as done: "{tasks[index]["title"]}"')


def delete_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to delete. Add one first!")
        return
    view_tasks(tasks)
    
    num = input("\nEnter the task number to delete: ").strip()
    if not num.isdigit():
        print("\n⚠️ Please enter a valid number.")
        return
    
    index = int(num) - 1
    if index < 0 or index >= len(tasks):
        print("⚠️ That number is not in the list.")
        return
    
    removed = tasks.pop(index)
    print(f'\n🗑️ Deleted: "{removed["title"]}"')


main()