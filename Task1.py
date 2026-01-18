
a = input("Enter a task: ")
with open("todo.txt", "a") as f:   
    f.write(a + "\n")
print("Task added successfully")

with open("todo.txt", "r") as f:
    tasks = f.readlines()

if len(tasks) == 0:
    print("No tasks found")
else:
    print("\nYour Tasks:")
    for i in range(len(tasks)):
        print(i + 1, tasks[i].strip())

c = int(input("\nEnter task number to delete: "))

if 1 <= c <= len(tasks):
    tasks.pop(c - 1)  
    with open("todo.txt", "w") as f:
        f.writelines(tasks)
    print("Task deleted successfully")
else:
    print("Invalid task number")


