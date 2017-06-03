class Person():

    def __init__(self, name, age):
        # we set some private variables such as age and name
        self._name = name
        self._age = age

    # we use getters so that we dont break ADT
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

class Teacher(Person):

    def __init__(self, name, age, subject):
        # Since we inherit Person, we can call it's init method
        Person.__init__(self, name, age)
        self._subject = subject

    # we can also add our own new method
    def get_subject(self):
        return self._subject

    # what happens if we uncomment this? Remember that Person also has
    # a get_age() method
    def get_age(self):
        return self.get_name() + "'s age is " + str(self._age)

if (__name__ == "__main__"):
    person = Person("Brian", 20)
    teacher = Teacher("Brian", 20, "Computer Science")
    print("Person:", person.get_name(), person.get_age())
    print("Teacher:", teacher.get_name(), teacher.get_age(), teacher.get_subject())
