""" Task 36. Company`s Checkpoint """
import time
import uuid
import datetime
import random


def time_return():
    time.sleep(2)


class Person:

    def __init__(self, name, position, department, working_hours, id_=None, bank_info=None, **kwargs):
        """System: Initializes the Person class of the employee...."""
        self.name = name.title()
        self.position = position.capitalize()
        self.department = department.upper()
        self.working_hours = working_hours
        self.__id = id_
        self.bank_info = bank_info
        for key, value in kwargs.items():
            self.key = key
            self.value = value

    def say(self):
        """Employee says...."""
        print(f"{self.name} says: > Hi, I`m a {self.position} from {self.department} departament.\n")

    def get_id(self):
        """System: Returns the works ID of the employee...."""
        if self.__id is not None:
            return self.__id
        else:
            self.__id = uuid.uuid4()
            return self.__id

    def get_time_exit(self):
        """System: Returns the time of the employee's exit from work...."""
        return datetime.datetime.now() + datetime.timedelta(hours=self.working_hours)

    def get_bank_info(self):
        """System: Returns the bank information of the employee...."""
        self.bank_info = [uuid.uuid4(), random.randint(1000000, 1000000000)]
        return self.bank_info


class Subordinate(Person):

    salary = 5000

    def __init__(self, name, position, department, working_hours, **kwargs):
        """System: Initializes the Subordinate class of the Subordinate...."""
        super().__init__(name, position, department, working_hours, id_=None, bank_info=None, **kwargs)
        for key, value in kwargs.items():
            self.key = key.capitalize()
            self.value = value

    def get_projects(self):
        """System: Returns the name of projects of the Subordinate...."""
        return self.key

    def get_bonus(self):
        """System: Returns the bonus in $ of the Subordinate...."""
        return self.salary * self.value / 100

    def get_total_salary(self):
        """System: Returns the total salary in $ of the Subordinate...."""
        return self.salary + self.get_bonus()

    def get_info_worker(self):
        """System: Returns the information about the Subordinate...."""
        print(f"-> Subordinate: {self.name}\n-> ID: {self.get_id()}\n"
              f"-> Position: {self.position}\n"
              f"-> Department: {self.department}\n"
              f"-> Time of entry to work: {datetime.datetime.now()}\n"
              f"-> Working hours: {self.working_hours}\n"
              f"-> Time of exit from work: {self.get_time_exit()}\n"
              f"-> Financial data of {self.name}:\n-> Salary: {self.salary}$\n"
              f"-> Bank account > [ID account : Checking account] > {self.get_bank_info()}\n"
              f"-> Latest data of {self.name}:\n-> Project: {self.get_projects()}\n"
              f"-> Bonus of the doing projects: {self.get_bonus()}$\n"
              f"-> Income with bonus: {self.get_total_salary()}$\n")

    @classmethod
    def change_salary(cls, new_salary):
        """Changes the salary of the Subordinate...."""
        cls.salary = new_salary
        return cls.salary


class Supervisor(Person):

    rating = 99.8

    def __init__(self, name, position, department, working_hours, **kwargs):
        """System: Initializes the Supervisor class of the Supervisor...."""
        super().__init__(name, position, department, working_hours, id_=None, bank_info=None, **kwargs)
        for key, value in kwargs.items():
            self.key = key
            self.value = value

    def get_percent(self):
        """System: Returns the percent in $ of the Supervisor...."""
        return self.value * self.rating / 100

    def get_salary(self):
        """System: Returns the salary in $ of the Supervisor...."""
        return self.value + self.get_percent()

    def get_info_worker(self):
        """System: Returns the information about the Supervisor...."""
        print(f"-> Supervisor: {self.name}\n-> ID: {self.get_id()}\n-> Position: {self.position}\n-> Department: {self.department}\n"
              f"-> Leader rating: {self.rating}\n"
              f"-> Time of entry to work: {datetime.datetime.now()}\n-> Working hours: {self.working_hours}\n"
              f"-> Time of exit from work: {self.get_time_exit()}\n"
              f"-> Financial data of {self.name}:\n-> Salary: {self.value}$\n"
              f"-> Bank account > [ID account : Checking account] > {self.get_bank_info()}\n"
              f"-> Percent of the salary in $: {self.get_percent()}$\n"
              f"-> Income with bonus: {self.get_salary()}$\n")

    @classmethod
    def change_rating(cls, new_rating):
        """Changes the rating of the Supervisor...."""
        cls.rating = new_rating
        return cls.rating


class Company:

    def __init__(self, name):
        """System: Initializes the Company class of the company...."""
        self.name = name.title()
        self.subordinate = []
        self.supervisor = []
        self.person_list = []

    def add_subordinate(self, subordinate):
        """System: Adds the subordinate to the company...."""
        return self.subordinate.append(subordinate)

    def add_supervisor(self, supervisor):
        """System: Adds the supervisor to the company...."""
        return self.supervisor.append(supervisor)

    def add_uuid(self, person):
        """System: Adds the uuid to the employee in DB...."""
        return self.person_list.append(person)

    def show_persons(self):
        """System: Shows all employees of the company...."""
        print(f"->  Employees of {self.name}:")
        for subordinate in self.subordinate:
            print(f"  Subordinate: {subordinate.name}")
        for supervisor in self.supervisor:
            print(f"  Supervisor: {supervisor.name}")

    def check_worker(self, person):
        """System: Level 1 -> Checks the employee in DB...."""
        if person not in self.supervisor + self.subordinate:
            print(f"WARRNING!!! {person.name} -> This person does not work for company {self.name}!")
        else:
            for item in self.supervisor or self.subordinate:
                assert item in self.supervisor or self.subordinate, f"{person.name} -> ID not found in the database!"
                print(f'-> Result: {person.name} > Identity verification completed...\n'
                      f'-> Result: {person.name} > SUCCESSFULLY\n')

    def check_uuid(self, person):
        """System: Level 2 -> Checks the uuid of the employee in DB...."""
        if person not in self.supervisor + self.subordinate:
            print(f"WARRNING!!! {person.name} -> This person does not work for company {self.name}!")
        else:
            for item in self.person_list:
                assert item in self.person_list, f"{person.name} -> Your ID not found in the database!"
                assert isinstance(item, uuid.UUID), f"{person.name} -> Your ID is not class <UUID>!"
            print(f'-> Result: {person.name} > Identity verification completed...\n'
                  f'-> Result: {person.name} > SUCCESSFULLY\n')

    def general_check_worker(self, person):
        """System: Level 3 -> General check to employee in DB...."""
        if person not in self.supervisor + self.subordinate:
            print(f"WARRNING!!! {person.name} -> This person does not work for company {self.name}!")
        else:
            for item in self.supervisor + self.subordinate:
                assert item in self.supervisor + self.subordinate, f"{person.name} -> ID not found in the database!"
            for item in self.person_list:
                assert item in self.person_list, f"{person.name} -> Your ID not found in the database!"
                assert isinstance(item, uuid.UUID), f"{person.name} -> Your ID is not class <UUID>!"
            print(f'-> Result: {person.name} > Identity verification completed...\n'
                  f'-> Result: {person.name} > SUCCESSFULLY\n')

    def global_employee_verification(self, person):
        """System: Level 4 -> Global employee verification in DB...."""
        if person not in self.supervisor + self.subordinate:
            print(f"WARRNING!!! {person.name} -> This person does not work for company {self.name}!")
        else:
            if person in self.supervisor:
                for supervisor in self.supervisor:
                    assert isinstance(supervisor, Supervisor), f"{person.name} -> This is not a class <Supervisor>!"
                    assert isinstance(supervisor, Person), f"{person.name} -> This is not a class <Person>!"
                print(f'-> Result: {person.name} > Verification of supervisor completed...\n'
                      f'-> Result: {person.name} > SUCCESSFULLY\n'
                      f'-> {person.name} is ALLOWED ENTRY to the company {self.name}\n')
            elif person in self.subordinate:
                for subordinate in self.subordinate:
                    assert isinstance(subordinate, Subordinate), f"{person.name} -> This is not a class <Subordinate>!"
                    assert isinstance(subordinate, Person), f"{person.name} -> This is not a class <Person>!"
                print(f'-> Result: {person.name} > Verification of subordinate completed...\n'
                      f'-> Result: {person.name} > SUCCESSFULLY\n'
                      f'-> {person.name} is ALLOWED ENTRY to the company {self.name}\n')

    def get_result_request_of_company(self, person):
        """System: Request -> Get information about the employee...."""
        print(f"System: Request from {self.name} > 'Get information about the employee {person.name}'....\n")
        if person not in self.supervisor + self.subordinate:
            print(f"-> WARRNING!!!{person.name} does not work for company {self.name}!\n"
                  f"-> Result: {person.name} > Verification of person completed...\n"
                  f"-> Result: {person.name} > UNSUCCESSFULLY\n"
                  f"-> {person.name} is DENIED ENTRY to company {self.name}\n"
                  f"-> {person.name}! Please contact the {self.name} security service or "
                  f"the appropriate person who made your appointment")
        else:
            return f"{time_return()}" \
                   f"{print(person.get_info_worker.__doc__)}\n" \
                   f"{time_return()}" \
                   f"{person.get_info_worker()}\n" \
                   f"{time_return()}" \
                   f"{print(company.check_worker.__doc__)}\n" \
                   f"{time_return()}" \
                   f"{company.check_worker(person)}\n" \
                   f"{time_return()}" \
                   f"{print(company.check_uuid.__doc__)}\n" \
                   f"{time_return()}" \
                   f"{company.check_uuid(person)}\n" \
                   f"{time_return()}" \
                   f"{print(company.general_check_worker.__doc__)}\n" \
                   f"{time_return()}" \
                   f"{company.general_check_worker(person)}\n" \
                   f"{time_return()}" \
                   f"{print(company.global_employee_verification.__doc__)}\n" \
                   f"{time_return()}" \
                   f"{company.global_employee_verification(person)}\n"


company = Company("limelight networks")
user1 = Subordinate("daria veresha", "junior", "IT", 12,
                    django_Project=10)
user2 = Supervisor("alex litvinov", "senior", "IT", 8,
                   salary=12000)
user3 = Subordinate("jon smith", "trainee", "IT", 12,
                    flask_Project=5)

print(company.add_subordinate.__doc__)
company.add_subordinate(user1)
time_return()
print(company.add_supervisor.__doc__)
company.add_supervisor(user2)
time_return()
print(company.add_uuid.__doc__)
company.add_uuid(user1.get_id())
time_return()
print(company.add_uuid.__doc__)
company.add_uuid(user2.get_id())
time_return()
print(company.show_persons.__doc__)
time_return()
company.show_persons()
print('--------------------------------------------------')
time_return()
user1.say()
time_return()
company.get_result_request_of_company(user1)
print('-------------------------------------------------')
time_return()
user2.say()
time_return()
company.get_result_request_of_company(user2)
print('-------------------------------------------------')
time_return()
user3.say()
time_return()
company.get_result_request_of_company(user3)











































