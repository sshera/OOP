# def hello():
# print("hello")

# print(type(hello))

# string = "hello"
# print(string.upper())


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name)
        # runs immediately as soon as new dog is defined

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Rex", 3)
d2 = Dog("Duke", 8)
# print(type(d))
# print(d.add_one(3))
# d.bark()
# print(d2.get_name())
# print(d2.get_age())
# print(d.get_name())
# d.set_age(2)
# print(d.get_age())


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # between 0 and 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
# print(course.students[0].name)
print(course.get_average_grade())
