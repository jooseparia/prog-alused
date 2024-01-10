"""Simple class."""


class Student:
    """Student class."""

    def __init__(self, name):
        """Student class construct.

        Creates student type object.
        Parameters:
        n (str): Name of student.
        """
        self.name = name
        self.finished = False
