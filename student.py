'''
02
This is a class defining a techer in a school.

Usage:
    1.Create a new student:
        s= Student(ID, student_name, student_family , address, phone_nuumber, major, sex, interance_year)

   2. Print the teacher info:    
        print(s)
'''


class Student:
    def __init__(self, ID, name, family, address, phone, major, sex, year):
        self.__ID = ID
        self.__name = name
        self.__family = family
        self.__address = address
        self.__phone = phone
        self.__major = major

        if sex not in ['male', 'female']:
            raise ValueError('The value should be either "male" or "female".')
        self.__sex = sex
        
        self.__year = year

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
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        self.__family = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        if value not in ['male', 'female']:
            raise ValueError('The value of sex should be either "male" or "female".')
        self.__sex = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def __str__(self):
        return 'ID: {}\nName: {} {}\nAddress: {}\nPhone: {}\nMajor: {}\nSex: {}\nYear: {}'.format(
            self.ID, self.name, self.family, self.address, self.phone, self.major, self.sex, self.year
        )


class GraduateStudent(Student):
    def __init__(self, ID, name, family, address, phone, major, sex, year, yearofgraduate):
        super().__init__(ID, name, family, address, phone, major, sex, year)
        self.__yearofgraduate = yearofgraduate

    @property
    def yearofgraduate(self):
        return self.__yearofgraduate

    @yearofgraduate.setter
    def yearofgraduate(self, value):
        self.__yearofgraduate = value

    def __str__(self):
        return super().__str__() + '\nYear of Graduate: {}'.format(self.yearofgraduate)


# Usage:
#s = Student(9920049, 'Hiva', 'Nazeri', 'Iran, Tehran', '09123093847', 'Computer Science', 'female', 1402)
#print(s)

#s1 = GraduateStudent(1234, 'Maryam', 'Mirzakhani', 'Tehran', '091284848', 'Mathematics', 'female', 1395, 1399)
#print(s1)
