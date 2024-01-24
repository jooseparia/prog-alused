"""Encapsulation exercise."""


class Student:
    """Represent a student with encapsulated attributes and methods."""

    def __init__(self, name, id):
        """
        Initialize a new Student object.

        Parameters:
        - name (str): The name of the student.
        - id (int): The unique identifier for the student.
        """
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self):
        """
        Get the student's ID.

        Returns:
        - int: The student's ID.
        """
        return self.__id

    def set_name(self, name):
        """
        Set the student's name.

        Parameters:
        - name (str): The new name for the student.
        """
        self.__name = name

    def get_name(self):
        """
        Get the student's name.

        Returns:
        - str: The student's name.
        """
        return self.__name

    def set_status(self, status):
        """
        Set the student's status.

        Parameters:
        - status (str): The new status for the student.

        Valid statuses: "Active", "Expelled", "Finished", "Inactive"
        """
        valid_statuses = {"Active", "Expelled", "Finished", "Inactive"}
        if status in valid_statuses:
            self.__status = status

    def get_status(self):
        """
        Get the student's status.

        Returns:
        - str: The student's status.
        """
        return self.__status
