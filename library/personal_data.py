from datetime import datetime

from utils.exceptions import (
    EmailAddressException,
    PhoneNumberException,
    DateOfBirthException,
    EmployeeNumberException,
    AgeRestrictionException,
    NotEmployeeException)


class Person:
    """This is a generic person object."""

    PHONE_NUMBER_LENGTH = 13
    DOB_LENGTH = 10

    # attributes
    first_name = ""
    last_name = ""
    phone_number = ""
    email_address = ""
    date_of_birth = None

    # constructor
    def __init__(self,
                 first_name,
                 last_name,
                 phone_number,
                 email_address,
                 date_of_birth):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = self.validate_phone_number(phone_number)
        self.email_address = self.validate_email_address(email_address)
        self.date_of_birth = self.validate_date_of_birth(date_of_birth)

    # to string override method
    def __str__(self):
        """Print name to screen."""
        return "{}, {}, age {}".format(self.first_name, self.last_name, self.get_age())

    def validate_email_address(self, email_address):
        if "@" in email_address:
            return email_address

        raise EmailAddressException(email_address)

    def validate_phone_number(self, phone_number):
        if "+" in phone_number and len(phone_number) == self.PHONE_NUMBER_LENGTH:
            return phone_number

        raise PhoneNumberException(phone_number)

    def validate_date_of_birth(self, date_of_birth):
        if "/" in date_of_birth and len(date_of_birth) == self.DOB_LENGTH:
            dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
            return dob

        raise DateOfBirthException(date_of_birth)

    def get_age(self):
        year_now = datetime.today().year
        age_year = self.date_of_birth.year
        return year_now - age_year


class Employee(Person):
    """This is an employee object."""

    # constant
    AGE_LIMIT = 18
    EMPLOYEE_NUMBER_LENGTH = 8

    # attributes
    employee_number = ""

    def __init__(self, *args, **kwargs):
        employee_number = kwargs.pop("employee_number")
        super().__init__(*args, **kwargs)
        self.employee_number = self.validate_employee_number(employee_number)
        self.validate_employment_age()

    def validate_employee_number(self, employee_number):
        if len(employee_number) == self.EMPLOYEE_NUMBER_LENGTH and employee_number.isnumeric():
            return employee_number

        raise EmployeeNumberException(employee_number)

    def validate_employment_age(self):
        year_now = datetime.today().year
        min_employment_age_year = year_now - self.AGE_LIMIT
        if self.date_of_birth.year > min_employment_age_year:
            raise AgeRestrictionException(self.first_name, self.last_name)


class Manager(Employee):
    """ This Employee is a Manager."""
    employees = list()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise NotEmployeeException(employee.first_name, employee.last_name)

    def list_employee(self):
        list_employees = []
        for employee in self.employees:
            list_employees.append(str(employee))

        return list_employees
