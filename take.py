'''
04
This is a class defining a take in a school.

Usage:
   1) Create a new take:
        tk= Take(student, teacher, course, year, semester, grade)

   2) Print the course information:    
        print(tk) 
'''

from student import Student, GraduateStudent
from teacher import Teacher
from course import Course

class Take:
     def __init__(self, student, teacher, course, year, semester, grade = None): 
          self.__student = student
          self.__teacher = teacher
          self.__course = course         
          self.__year = year

          if semester not in [1,2]: 
               raise ValueError('the semester should be 1 or 2')          
          
          self.__semester = semester
          if grade and (grade >20 or grade<0):
               raise ValueError('the value of grade should be in [0,20]')
          self.__grade = grade


     #setters and getters
     @property
     def student(self):
          return self.__student
     
     @student.setter
     def ID(self,value): 
          self.__student = value
     
     @property
     def teacher(self):
          return self.__teacher
     
     @teacher.setter
     def teacher(self,value): 
          self.__teacher = value
     
     @property
     def course(self):
          return self.__course
     
     @course.setter
     def ID(self,value): 
          self.__course = value

     @property
     def year(self): 
          return self.__year

     @year.setter
     def year(self,value): 
          self.__year = value
     
     @property
     def semester(self): 
          return self.__semester

     @semester.setter
     def semester(self,value): 
          if value not in [1,2]: 
               raise ValueError('the semester should be 1 or 2')
          self.__semester = value

     @property
     def grade(self): 
          return self.__grade

     @grade.setter
     def grade(self,value): 
          if value >20 or value<0:
               raise ValueError('the value of grade should be in [0,20]')
          self.__grade = value
     

     def __str__(self): 
        return 'STUDENT --> {}\t\tTEACHER --> {}\t\tCOURSE --> {}\t\tyear: {}\tsemester: {}\tgrade: {}'\
            .format(self.student.ID,self.teacher.ID, self.course.ID, self.year, self.semester, self.grade)

'''
s = Student(343, 'Maryam', 'Alipur', 'Guilan, Rasht', '0911833838', 'mathematics', 'female', 1399)
t = Teacher(123, 'Ali', 'Jamali', 'Guilan, Rasht', '09112383822', 'Computer Science', 'male', 'assistant professor' )
c = Course('db232', 'database', 3)
tk = Take(s, t, c, 1400, 2)
print(tk)
s1 = GraduateStudent(343, 'Maryam', 'Alipur', 'Guilan, Rasht', '0911833838', 'applied mathematics', 'female', 1399,'AI')
tk1 = Take(s1, t, c, 1400, 3, 12)
print(tk1)
'''