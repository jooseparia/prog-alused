"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname, and age."""

    def __init__(self):
        """
        Initialize a new Person object with default values.

        Attributes:
        - firstname (str): The first name of the person.
        - lastname (str): The last name of the person.
        - age (int): The age of the person.
        """
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname, and age."""

    def __init__(self, firstname, lastname, age):
        """
        Initialize a new Student object.

        Parameters:
        - firstname (str): The first name of the student.
        - lastname (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty_instance = Empty()

    # 3 x person usage
    person1 = Person("Matthias", "Jarvet", 16)
    person2 = Person("Riivo", "Meremae", 18)
    person3 = Person("Rannar", "Jarvsoo", 19)

    # 3 x student usage
    student1 = Student("Marten", "Nommkula", 14)
    student2 = Student("Karl", "Kutt", 17)
    student3 = Student("Anu", "Mai", 47)

    # Displaying information
    print("Empty instance:", empty_instance)

    print("\nPerson instances:")
    print(person1.firstname, person1.lastname, person1.age)
    print(person2.firstname, person2.lastname, person2.age)
    print(person3.firstname, person3.lastname, person3.age)

    print("\nStudent instances:")
    print(student1.firstname, student1.lastname, student1.age)
    print(student2.firstname, student2.lastname, student2.age)
    print(student3.firstname, student3.lastname, student3.age)
