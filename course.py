'''
01
This is a class defining a course in a school.

Usage: 
    1.Create a new course:
        c = Course(ID, name, year)
    2. Print the course info:
        print(c)
'''

class Course:
    def __init__(self, ID, name, year):
        self.__ID = ID
        self.__name = name
        self.__year = year
        # we can also define an "if" condition to control the year given for the course

    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, value):
        self.__ID = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        self.__year = value

    def __str__(self):
        return 'ID:{} Name:{} Year:{}'.format(self.ID, self.name, self.year)
    

# Usage:
#c = Course(400221, "Math", 1400)
#print(c)