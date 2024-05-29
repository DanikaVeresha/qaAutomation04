""" Task 36. Company`s Checkpoint """
import time
import uuid
import datetime
import random
from abc import abstractmethod


class Person:

    def __init__(self, name, position, department, working_hours, __id=None, bank_info=None, **kwargs):
        """System: Initializes the Person class of the person...."""
        self.name = name.title()
        self.position = position.capitalize()
        self.department = department.upper()
        self.working_hours = working_hours
        self.__id = __id
        self.bank_info = bank_info
        for key, value in kwargs.items():
            self.key = key
            self.value = value

    def say(self):
        """Person says...."""
        print(f"{self.name} says: -> Hi, I`m a {self.position} from {self.department} departament.\n")

    def get_id(self):
        """System: Returns the works ID of the person...."""
        if self.__id is not None:
            return self.__id
        else:
            self.__id = uuid.uuid4()
            return self.__id

    def get_time_exit(self):
        """System: Returns the time of the person's exit from work...."""
        return datetime.datetime.now() + datetime.timedelta(hours=self.working_hours)

    def get_bank_info(self):
        """System: Returns the bank information of the person...."""
        self.bank_info = [uuid.uuid4(), random.randint(1000000, 1000000000)]
        return self.bank_info


class Subordinate(Person):

    salary = 5000

    def __init__(self, name, position, department, working_hours, **kwargs):
        """System: Initializes the Subordinate class of the Subordinate...."""
        super().__init__(name, position, department, working_hours, __id=None, bank_info=None, **kwargs)
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

    def get_info_about_subWorker(self):
        """System: Returns the information about the Subordinate...."""
        return f"{self.name}\nID: {self.get_id()}\n" \
               f"Bank account -> [ID account : Checking account]: {self.get_bank_info()}\n" \
               f"Latest data:\nProject: {self.get_projects()}\n" \
               f"Bonus of the doing projects: {self.get_bonus()}\n" \
               f"Income with bonus: {self.get_total_salary()}"

    @classmethod
    def change_salary(cls, new_salary):
        """Changes the salary of the Subordinate...."""
        cls.salary = new_salary
        print(f'-> {cls.salary}$\n')


class Supervisor(Person):

    rating = 98.6

    def __init__(self, name, position, department, working_hours, **kwargs):
        """System: Initializes the Supervisor class of the Supervisor...."""
        super().__init__(name, position, department, working_hours, __id=None, bank_info=None, **kwargs)
        for key, value in kwargs.items():
            self.key = key
            self.value = value

    def get_percent(self):
        """System: Returns the percent in $ of the Supervisor...."""
        return self.value * self.rating / 100

    def get_salary(self):
        """System: Returns the salary in $ of the Supervisor...."""
        return self.value + self.get_percent()

    def get_info_about_supWorker(self):
        """System: Returns the information about the Supervisor...."""
        return f"{self.name}\nID: {self.get_id()}\n" \
               f"Bank account -> [ID account : Checking account]: {self.get_bank_info()}\n" \
               f"Accounting information:\nPercent of the salary: {self.get_percent()}\n" \
               f"Income with bonus: {self.get_salary()}"

    @classmethod
    def change_rating(cls, new_rating):
        """Changes the rating of the Supervisor...."""
        cls.rating = new_rating
        print(cls.rating)


class Company:

    def __init__(self, name):
        """System: Initializes the Company class of the company...."""
        self.name = name
        self.subordinate = []
        self.supervisor = []
        self.person_list = []

    def add_subordinate(self, subordinate):
        """System: Adds the subordinate to the company in DB...."""
        return self.subordinate.append(subordinate)

    def add_supervisor(self, supervisor):
        """System: Adds the supervisor to the company in DB...."""
        return self.supervisor.append(supervisor)

    def add_uuid(self, person):
        """System: Adds the uuid to the person in DB...."""
        return self.person_list.append(person)

    def show_persons(self):
        """System: Shows all work persons of the company...."""
        print(f"->  Workers of {self.name}:")
        for subordinate in self.subordinate:
            print(f"  Subordinate: {subordinate.name}")
        for supervisor in self.supervisor:
            print(f"  Supervisor: {supervisor.name}")

    def check_worker(self, person):
        """System: Checks the worker in DB...."""
        for item in self.supervisor + self.subordinate:
            assert item in self.supervisor + self.subordinate, f"{person.name} -> Your ID not found in the database!"
        print(f'-> Level 1: {person.name} - Identity verification completed successfully!\n')

    def check_uuid(self, person):
        """System: Checks the uuid of the person in DB...."""
        for item in self.person_list:
            assert item in self.person_list, f"{person.name} -> Your ID not found in the database!"
            assert isinstance(item, uuid.UUID), f"{person.name} -> Your ID is not class <UUID>!"
        print(f'-> Level 2: {person.name} - Identity verification completed successfully!\n')

    def global_check_worker(self, person):
        """System: Global Checks the worker in DB...."""
        for item in self.supervisor + self.subordinate:
            assert item in self.supervisor + self.subordinate, f"{person.name} -> ID not found in the database!"
        for item in self.person_list:
            assert item in self.person_list, f"{person.name} -> Your ID not found in the database!"
            assert isinstance(item, uuid.UUID), f"{person.name} -> Your ID is not class <UUID>!"
        print(f'-> Level 3: {person.name} - Identity verification completed successfully!\n')

    def verification_subordinate(self, person):
        """System: Verifies the subordinate in DB...."""
        for subordinate in self.subordinate:
            assert isinstance(subordinate, Subordinate), f"{person.name} -> This is not a class <Subordinate>!"
            assert isinstance(subordinate, Person), f"{person.name} -> This is not a class <Person>!"
        print(f'-> Level 4: {person.name} - Verification of subordinates completed successfully!\n')

    def verification_supervisor(self, person):
        """System: Verifies the supervisor in DB...."""
        for supervisor in self.supervisor:
            assert isinstance(supervisor, Supervisor), f"{person.name} -> This is not a class <Supervisor>!"
            assert isinstance(supervisor, Person), f"{person.name} -> This is not a class <Person>!"
        print(f'-> Level 4: {person.name} - Verification of supervisors completed successfully!\n')


company = Company("EPAM")
user1 = Subordinate("josh smith", "junior", "IT", 12,
                           django_Project=10)
user2 = Supervisor("nik douson", "senior", "IT", 8,
                         salary=12000)
print(company.add_subordinate.__doc__)
company.add_subordinate(user1)
print(company.add_supervisor.__doc__)
company.add_supervisor(user2)
print(company.add_uuid.__doc__)
company.add_uuid(user1.get_id())
print(company.add_uuid.__doc__)
company.add_uuid(user2.get_id())
print(company.show_persons.__doc__)
company.show_persons()
print()
print('--------------------------------------------------')
print(user1.say.__doc__)
user1.say()
print(company.check_worker.__doc__)
company.check_worker(user1)
print(company.check_uuid.__doc__)
company.check_uuid(user1)
print(company.global_check_worker.__doc__)
company.global_check_worker(user1)
print(company.verification_subordinate.__doc__)
company.verification_subordinate(user1)
# print(company.verification_subordinate.__doc__)
# company.verification_subordinate()
# print()
# print(company.show_secur_info_subordinate.__doc__)
# company.show_secur_info_subordinate()
print('-------------------------------------------------')
print(user2.say.__doc__)
user2.say()
print(company.check_worker.__doc__)
company.check_worker(user2)
print(company.check_uuid.__doc__)
company.check_uuid(user2)
print(company.global_check_worker.__doc__)
company.global_check_worker(user2)
print(company.verification_supervisor.__doc__)
company.verification_supervisor(user2)
# print(company.verification_supervisor.__doc__)
# company.verification_supervisor()
# print()
# print(company.show_secur_info_supervisor.__doc__)
# company.show_secur_info_supervisor()












































