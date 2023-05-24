'''
05
This is a class defining a department in a school.
Department is a collection of "students","teachers"&"courses".
students take courses with a teacher.
Any Department has a "Department Manager".

Usage:
    d = Department(String department_name, String phone_number)
'''
from student import Student, GraduateStudent
from teacher import Teacher
from course import Course
from take import Take
import pickle

class Department: 
    def __init__(self, id, name, manager, phone, students = [], teachers = [], courses = [], takes = [] ): 
        self.__id = id
        self.__name = name
        self.__manager = manager
        self.__phone = phone
        self.__student_file = r'data\{}_students.dat'.format(self.__id)
        self.__teacher_file = r'data\{}_teachers.dat'.format(self.__id)
        self.__course_file = r'data\{}_courses.dat'.format(self.__id)
        self.__take_file = r'data\{}_takes.dat'.format(self.__id)
        self.__students = students
        self.__teachers = teachers
        self.__courses = courses
        self.__takes = takes
    
    #setters and getters

    @property
    def ID(self):
        return self.__id
     
    @ID.setter
    def ID(self,value): 
        self.__id = value
    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def manager(self):
        return self.__manager
     
    @manager.setter
    def manager(self,value): 
        self.__manager = value
    
    @property
    def phone(self): 
        return self.__phone

    @phone.setter
    def phone(self,value): 
        self.__phone = value

    @property
    def students(self): 
        return self.__students

    @property
    def teachers(self): 
        return self.__teachers
    
    @property
    def courses(self): 
        return self.__courses
    
    @property
    def takes(self): 
        return self.__takes

    
    #helper methods to save/read data in/from files
    def __save_students(self): 
        with open(self.__student_file, 'wb') as file:
            pickle.dump(self.students, file)

    def __read_students(self): 
        with open(self.__student_file, 'rb') as file:
            self.__students = pickle.load(file)
    
    def __save_teachers(self): 
        with open(self.__teacher_file, 'wb') as file:
            pickle.dump(self.teachers, file)

    def __read_teachers(self): 
        with open(self.__teacher_file, 'rb') as file:
            self.__teachers = pickle.load(file)
    
    def __save_courses(self): 
        with open(self.__course_file, 'wb') as file:
            pickle.dump(self.courses, file)

    def __read_courses(self): 
        with open(self.__course_file, 'rb') as file:
            self.__courses = pickle.load(file)

    def __save_takes(self): 
        with open(self.__take_file, 'wb') as file:
            pickle.dump(self.takes, file)

    def __read_takes(self): 
        with open(self.__take_file, 'rb') as file:
            self.__takes = pickle.load(file)
    
    def save_to_file(self): 
        self.__save_students()
        self.__save_takes()
        self.__save_courses()
        self.__save_teachers()

    def read_from_file(self): 
        self.__read_students()
        self.__read_courses()
        self.__read_takes()
        self.__read_teachers()
    
    #add or remove elements 
    def __add__(self, element): 
        if type(element) is Student: 
            if element not in self.__students:
                self.__students.append(element)
        
        elif type(element) is Teacher: 
            if element not in self.__teachers:
                self.__teachers.append(element)
        
        elif type(element) is Course: 
            if element not in self.__courses:
                self.__courses.append(element)
        
        elif type(element) is Take: 
            if element not in self.__takes:
                self.__takes.append(element)
        
        else: 
            raise ValueError('the element you want to add should be of types [Student, Teacher, Course, Take]')
        
        return self

    def __sub__(self, element): 
        if type(element) is Student: 
            if element  in self.__students:
                self.__students.remove(element)
        
        elif type(element) is Teacher: 
            if element  in self.__teachers:
                self.__teachers.remove(element)
        
        elif type(element) is Take: 
            if element  in self.__takes:
                self.__takes.remove(element)
        
        else: 
            raise ValueError('the element you want to add should be of types [Student, Teacher, Course, Take]')
        
        return self


    def __str__(self): 
        S = '\n\n______________________________________________________________________________________________________\n\n'
        S += 'Department Name: {}    Manager: {} {}     Phone Number: {}'.format(self.name, self.manager.name, self.manager.family, self.phone)
        S += '\n\n____________________________________________STUDENTS___________________________________________________\n\n'
        
        for i in self.students: 
            S += '%s\n'%(i) 
        
        S += '\n\n____________________________________________TEACHERS___________________________________________________\n\n'        
        for i in self.teachers:
            S += '%s\n'%(i) 
        
        S += '\n\n____________________________________________COURCES___________________________________________________\n\n'        
        for i in self.courses:
            S += '%s\n'%(i) 

        S += '\n\n____________________________________________TAKES___________________________________________________\n\n'        
        for i in self.takes:
            S += '%s\n'%(i)

        S += '_______________________________________________________________________________________________________'
        return S


s1 = Student(123, 'ali', 'alipur', 'rasht', '09129393994', 'cp', 'male', 1400)
s2 = Student(124, 'Maryam', 'Valipour', 'rasht', '09179393994', 'cp', 'female', 1397)
s3 = Student(125, 'Reza', 'Kashani', 'rasht', '09855593994', 'cp', 'male', 1400)


t1 = Teacher(333, 'ali' , 'jamali ', 'rasth', '09129393994', 'AI', 'male', 'assistant professor')
t2 = Teacher(444, 'Sara' , 'Mahdavi ', 'Tehran', '09129393994', 'Optimization', 'female', 'assistant professor')


c1 = Course('A122', 'Advance Programming', 2)
c2 = Course('A838', 'Artificial Intelligence', 2)


tk1 = Take(s1, t1, c1, 1400, 2)
tk2 = Take(s1, t2, c2, 1399, 1)
tk3 = Take(s2, t2, c2, 1400, 1, 20)

d = Department('DEP_CP','Computer Science', s1, '09112384848')
d = d+t1
d = d+t2 
d = d+s1
d = d+s2
d = d+s3

d = d+c1
d = d+c2

d = d+tk1
d = d+ tk2
d = d+ tk3
print(d)

d.save_to_file()

d = d - s1
d = d - t1
print(d)

d.read_from_file()
print(d)