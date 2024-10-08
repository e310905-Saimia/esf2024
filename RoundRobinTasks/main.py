import time
import tasks

# Define your tasks
def task1():
    print("Task 1 is running")
    time.sleep(1)

def task2():
    print("Task 2 is running")
    time.sleep(1)

def task3():
    print("Task 3 is running")
    time.sleep(1)

# Round-robin scheduler
while True:
    task1()
    task2()
    task3()
    tasks.task4()
    tasks.task5()
    tasks.task6()