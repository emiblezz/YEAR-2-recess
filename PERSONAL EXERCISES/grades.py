import matplotlib.pyplot as plt
from tabulate import tabulate
class Grade():
    def __init__(self,marks,m):
        self.marks=marks
        self.m=m
    
    def __str__(self):
        return
    def average(self):
        total=sum(self.marks)
        average=total/self.m #m is the total number of the subjects
        txt=f"{name} sat EXAMS for {subject} and scored {marks} respectively with an average of {average}"
        return txt

n=int(input("Enter the number of students in your class: "))
m=int(input("Please enter the number of subjects: "))
name=[]
subject=[]
marks=[]
student={"NAME":name,"Subject":subject,"Marks":marks}


d=1
while(d<=n):
    names=input(f"Please enter the name of the student {d}: ")
    name.append(names)
    i=1
    while(i<=m):
        subjects=input(f"Enter the name of the subject {i}: ")
        subject.append(subjects)
        mark=int(input(f"Enter marks for the subject{i}: "))
        marks.append(mark)
        i +=1
    d +=1
    print(student)
  
  
row1=["Name"]
row1.extend(name)
row2=["Subject"]
row2.extend(subject)
row3=["Marks"]
row3.extend(marks)
result2=[row1,row2,row3]
k=tabulate(student,headers="keys",tablefmt='psql')
plt.bar(subject,marks)
#plt.plot(subject,marks)
plt.xlabel('SUBJECTS')
plt.ylabel('MARKS')
plt.title('Students Marks')
plt.show()
#print(n)
#print(k)