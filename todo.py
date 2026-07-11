todos = []

def show_todos():
    if len(todos) ==0:
        print("No todos yet!")
    else:
        print("\nYour To-Do List:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
def add_todo():
    todo = input("Enter todo: ")
    todos.append(todo)
    print(f"'{todo}' added successfully!")
def remove_todo():
    show_todos() 
    num = nt(input("Enter todo number to remove: "))
    removed = todos.pop(num - 1)
    print(f"'{removed}' removed!")

while True:
    print("\n===== TO-DO APP =====")
    print("1. Show todos")
    print("2. Add todo")
    print("3. Remove todo")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        show_todos()
    elif choice == '2':
        add_todo()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
    
