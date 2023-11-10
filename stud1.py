class student:
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("rollno",self.rollno)
        print("name"+self.name)
        print("course"+self.course)
class test(student):
    def getmark(self,mark):
        self.mark=mark
    def display(self):
         print("total mark",self.mark)
r=int(input("enter the rollno"))
n=input("enter the name")
c=input("enter the course")
m=int(input("enter the mark"))
stud1=test()
stud1.getdata(r,n,c)
stud1.getmark(m)
stud1.displaystudent()
stud1.display()
