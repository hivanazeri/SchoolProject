'''
03
This is a class defining a techer in a school.

Usage:
    1.Create a new teacher:
        t= Teacher(ID, name, family , address, phone, field, degree, sex)

   2. Print the teacher info:    
        print(t)
'''
class Teacher:
    def __init__(self, ID, name, family, address, phone, field, sex, degree):
        self.__ID = ID
        self.__name = name
        self.__family = family
        self.__address = address
        self.__phone = phone
        self.__field = field

        if sex not in ['male', 'female']:
            raise ValueError('The value of sex should be either "male" or "female".')
        self.__sex = sex

        if degree not in ['lecturer', 'assistant professor', 'associate professor', 'full professor']:
            raise ValueError('The degree should be one of the following: "lecturer", "assistant professor", "associate professor", "full professor".')
        self.__degree = degree

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
    def field(self):
        return self.__field

    @field.setter
    def field(self, value):
        self.__field = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        if value not in ['male', 'female']:
            raise ValueError('The value of sex should be either "male" or "female".')
        self.__sex = value

    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, value):
        if value not in ['lecturer', 'assistant professor', 'associate professor', 'full professor']:
            raise ValueError('The degree should be one of the following: "lecturer", "assistant professor", "associate professor", "full professor".')
        self.__degree = value

    def __str__(self):
        return 'ID: {}\nName: {} {}\nAddress: {}\nPhone: {}\nField: {}\nSex: {}\nDegree: {}'.format(
            self.ID, self.name, self.family, self.address, self.phone, self.field, self.sex, self.degree
        )


# Usage:
#t = Teacher(1223, 'Ali', 'Alipour', 'Guilan, Rasht', '09112383822', 'Computer Science', 'male', 'assistant professor')
#print(t)
