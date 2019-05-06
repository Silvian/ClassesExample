from library.personal_data import Person, Employee, Manager


def main():
    veronica = Person(
        first_name="Veronica",
        last_name="Timofte",
        phone_number="+447746397894",
        email_address="lacri.tim@gmail.com",
        date_of_birth="12/04/1993",
    )
    silvian = Person(
        first_name="Silvian",
        last_name="Dragan",
        phone_number="+447446830627",
        email_address="silvian.dragan@gmail.com",
        date_of_birth="29/04/1989"
    )

    john_doe = Employee(
        first_name="John",
        last_name="Doe",
        phone_number="+447446123456",
        email_address="john.doe@email.com",
        date_of_birth="01/01/1970",
        employee_number="67367899",
    )

    cristina_yang = Person(
        first_name="Cristina",
        last_name="Yang",
        phone_number="+447746364783",
        email_address="cristinayang@gmail.com",
        date_of_birth="11/01/2004",
    )

    chris_meisser = Manager(
        first_name="Chris",
        last_name="Meisser",
        phone_number="+447736453674",
        email_address="chrismeisser@deliveroo.co.uk",
        date_of_birth="12/09/1980",
        employee_number="98476365"

    )

    chris_meisser.add_employee(john_doe)
    # chris_meisser.add_employee(silvian)

    print("person: {}".format(veronica))
    print("another person: {}".format(silvian))
    print("employee: {}".format(john_doe))
    print("person: {}".format(cristina_yang))
    print("manager: {} has employees {} ".format(
        chris_meisser,
        chris_meisser.list_employee())
    )


if __name__ == '__main__':
    main()
