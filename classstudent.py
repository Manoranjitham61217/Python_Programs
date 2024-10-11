class student_data:
    def __init__(self,name,dob,rollno,blood_group,dept,cgpa):
        self.name=name
        self.dob=dob
        self.rollno=rollno
        self.bg=blood_group
        self.dept=dept
        self.cgpa=None

    def set_cgpa(self,):
        self.cgpa=float(input())

    def change_dob(self,c_dob):
        self.dob=c_dob

    def change_bloodgrp(self,c_bloodgrp):
        self.bg=c_bloodgrp

    def display(self):
        return (f"Student Name: {self.name}\n"f"Date of Birth: {self.dob}\n"f"Roll Number: {self.rollno}\n"f"Blood Group: {self.bg}\n"f"Department: {self.dept}\n"f"CGPA: {self.cgpa:.2f}")

student1=student_data("Giri","15.03.2006","58","O+","AI&DS",'')
student2=student_data("Surya","27.03.2005","39","B+","AI&DS",'')
student3=student_data("Praba","30.09.2005","30","A+","AI&DS",'')

student1.set_cgpa()
student2.set_cgpa()
student3.set_cgpa()

student1.change_dob("11.03.2006")
student3.change_bloodgrp("B+")

print(student1.display())
print()
print(student2.display())
print()
print(student3.display())
print()
