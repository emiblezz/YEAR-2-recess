#1 context manager for file handling 
class FileManager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file=None
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self,exc_type, exc_value, tracebook):
        self.file.close()
         
with FileManager('Alemi.txt', 'w') as file:
    file.write('ALEMI BLESS IS MY NAME')
    
#2 context manager for a database assuming a database called Bless.db

import sqlite3

class DatabaseManager:
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.dbname)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

# Example usage:
# with DatabaseManager('Bless.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#    result = cursor.fetchall()
#    for row in result:
#        print(row)

#3 multi threading
import threading

def task_1():
    print("Executing Task 1")

def task_2():
    print("Executing Task 2")

def task_3():
    print("Executing Task 3")

# Creating threads for each task
thread_1 = threading.Thread(target=task_1)
thread_2 = threading.Thread(target=task_2)
thread_3 = threading.Thread(target=task_3)

# Starting the threads
thread_1.start()
thread_2.start()
thread_3.start()

# Waiting for all threads to finish
thread_1.join()
thread_2.join()
thread_3.join()

print("All tasks completed")

# multiprocessing
import multiprocessing
from multiprocessing import freeze_support

def function_1():
    print("Executing Function 1")

def function_2():
    print("Executing Function 2")

def function_3():
    print("Executing Function 3")

if __name__ == '__main__':
    freeze_support()

    # Creating processes for each function
    process_1 = multiprocessing.Process(target=function_1)
    process_2 = multiprocessing.Process(target=function_2)
    process_3 = multiprocessing.Process(target=function_3)

    # Starting the processes
    process_1.start()
    process_2.start()
    process_3.start()

    # Waiting for all processes to finish
    process_1.join()
    process_2.join()
    process_3.join()

    print("All functions completed")
