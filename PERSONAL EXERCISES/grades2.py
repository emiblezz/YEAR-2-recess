import matplotlib.pyplot as plt

class Grade:
    def __init__(self, marks, m):
        self.marks = marks
        self.m = m

    def average(self):
        total = sum(self.marks)
        average = total / self.m
        return average

n = int(input("Enter the number of students in your class: "))
m = int(input("Please enter the number of subjects: "))

# Create a dictionary to store the results for each student
results = {}
for d in range(1, n+1):
    names = input(f"Please enter the name of the student {d}: ")
    marks = []
    for i in range(1, m+1):
        mark = int(input(f"Enter marks for the subject{i}: "))
        marks.append(mark)
    results[names] = Grade(marks, m)

names = list(results.keys())
subjects=["MTC","ENG","SST","SCIE"]
scores = [results[name].marks for name in results]

plt.xlabel('SUBJECTS')
plt.ylabel('MARKS')
plt.title('Students Marks')

# Iterate over the names and scores, and plot a line for each student
for name, mark in zip(names, scores):
    plt.plot(subjects, mark, label=name)
plt.legend()
plt.show()
