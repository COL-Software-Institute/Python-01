##To-Do List

#List to store tasks

tasks = [] # global variable scope

def add_task():
    task = input("Enter A task :: ")
    tasks.append(task)

def display_task():
    for i in range(len(tasks)):
        print(f"{i}.{tasks[i]}")

def delete_task():
    display_task()
    if tasks:
        #error handling it is error handling concept in python it allows the program to catch and handle errors gracefully.,insted of crashing when an erros occurs
        try:
            task_number = int(input("Enter the task number :: "))
            if 0 < task_number <=len(tasks):
                removed_tasks = tasks.pop(task_number - 1)
                print(f"tash is removed{removed_tasks}")
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid Input Please eneter a number")

def main():
    while True:
        print("\nTo do List Application options")
        print("1.view task")
        print("2.add task")
        print("3.remove task")
        print("4.Exit")


        choice = input("Enter your choice:: ")

        if choice == "1":
            display_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__": ## program Execution
    main()


        


