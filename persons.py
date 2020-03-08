import unittest

class Person:
    def set_name(self, name, surname):
        self.name = name
        self.surname = surname

    def set_gender(self,gender):
        self.gender = gender

    def display(self):
        attr_value = self.__dict__
       # print(attr_value)
        for atr in attr_value:
            print(attr_value[atr])


class Teacher(Person):
    def __init__(self):
        self.position = 'teacher'

    def hours(self, hours_number):
        self.hours = hours_number


    def set_salary(self):
        self.salary = self.hours * 18.5

class Disciple(Person):
    def __init__(self):
        self.position = 'disciple'

    def clas(self):
        self.clas = clas

    def how_many_lessons(self, number):
        self.lessons = number

osoba_1 = Teacher()
osoba_1.set_name("mateusz","zawadzki")
#osoba_1.display()

osoba_2 = Disciple()
osoba_2.set_name("jenny", "jenkins")
osoba_2.clas = "3A"
osoba_2.how_many_lessons(42)
#soba_2.display()

class Test_Teacher(unittest.TestCase):

    def test_init(self):
        mati = Teacher()
        mati.set_name("mateusz", "walaszek")
        result = ""
        result += mati.name + " " + mati.surname
        expected = "mateusz walaszek"
        assert result == expected

    def test_salary(self):
        mati = Teacher()
        mati.hours(100)
        mati.set_salary()
        result = mati.salary
        expected = 1850
        assert result == expected

if __name__ == '__main__':
    unittest.main()

