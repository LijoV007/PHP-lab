class student:
    def  __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("rollno",self.rollno)
        print("name"+self.name)
        print("course"+self.course)
stud1=student(10,"jack","MCA")
stud2=student(11,"anu","MCA")
stud1.displaystudent()
stud2.displaystudent()
        
