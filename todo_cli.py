import os

task_list = []
task = ""

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        content = file.read()
        print(f" your current tasks are: \n {content}")

while task != "end":
    task = input("Enter a task if you want to end enter 'end': ")

    if task.lower() == "end":
        break

    task_list.append(task)

with open("tasks.txt", "a") as file:
    for task in task_list:
        file.write(task + "\n")

print(os.getcwd())