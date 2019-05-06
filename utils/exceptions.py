class PersonException(AttributeError):
    """Person exception abstract class.
       Override the string method.
    """
    first_name = ""
    last_name = ""

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        """Method must be implemented."""
        raise NotImplemented


class EmailAddressException(AttributeError):
    """Exception class for email address validation"""

    email_address = ""

    def __init__(self, email_address):
        self.email_address = email_address

    def __str__(self):
        return "The email address {} provided is invalid.".format(self.email_address)


class PhoneNumberException(AttributeError):
    """Exception class for phone number validation"""

    phone_number = ""

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return "The phone number {} provided is invalid.".format(self.phone_number)


class DateOfBirthException(AttributeError):
    """ Exception class for DOB"""

    date_of_birth = ""

    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    def __str__(self):
        return "The Date of Birth {} provided is invalid".format(self.date_of_birth)


class EmployeeNumberException(AttributeError):
    """ Exception class for Employee Number"""

    employee_number = ""

    def __init__(self, employee_number):
        self.employee_number = employee_number

    def __str__(self):
        return "The Employee Number {} provided is invalid".format(self.employee_number)


class AgeRestrictionException(PersonException):
    """ Exception Class for Under 18"""

    def __str__(self):
        return "The Employee {} {} is under 18 ".format(
            self.first_name,
            self.last_name
        )


class NotEmployeeException(PersonException):
    """ Exception Class for not an employee"""

    def __str__(self):
        return "The person {} {} is not an employee.".format(
            self.first_name,
            self.last_name
        )
