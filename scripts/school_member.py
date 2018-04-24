class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def desc(self):
        print('My name is {}, and I am {} years old.'.format(self.name, self.age), end=' ')


class Student(SchoolMember):
    """
    Student class which extends from SchoolMember
    """

    def __init__(self, name, age, grade):
        SchoolMember.__init__(self, name, age)
        self.grade = grade

    def desc(self):
        SchoolMember.desc(self)
        print('I am a grade {} student'.format(self.grade))

    def __str__(self):
        return 'Student object: name = {}, age = {}, grade = {}'.format(self.name, self.age, self.grade)


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def desc(self):
        SchoolMember.desc(self)
        print('My salary is {}'.format(self.salary))


student1 = Student('Jerry', 10, 3)
student1.desc()
print(student1)
print(Student.__doc__)

teacher1 = Teacher('Lily', 30, 5000)
teacher1.desc()
print(teacher1)

