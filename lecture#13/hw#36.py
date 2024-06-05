"""Task 36. Company`s Checkpoint"""
import time
import uuid
import datetime
import random


def delay_time():
    time.sleep(2)


class Person:

    def __init__(self, name, position, level, department, working_hours=None,
                 salary=None, bonus=None, id_employee=None, bank_account=None, bank_card=None):
        """Initializes the Person class...."""
        self.name = name.title()
        self.position = position.title()
        self.level = level.capitalize()
        self.department = department.upper()
        self.working_hours = working_hours
        self.salary = salary
        self.bonus = bonus
        self.__uuid = id_employee
        self.bank_account = bank_account
        self.bank_card = bank_card

    def say(self):
        """Person says...."""
        print(f"{self.name} says: > Hi, I`m a {self.position} from {self.department} departament.\n")

    def create_id(self):
        """Returns the employee identifier in uuid format...."""
        if self.__uuid is None:
            self.__uuid = uuid.uuid4()
        return self.__uuid

    def get_exit_time(self):
        """Returns the time the employee left work...."""
        return datetime.datetime.now() + datetime.timedelta(hours=self.working_hours)

    def create_bank_account(self):
        """Returns the bank information of the employee...."""
        if self.bank_account is None:
            self.bank_account = [
                uuid.uuid4(),
                random.randint(1000000, 1000000000)
            ]
        return self.bank_account

    def get_bonus(self):
        """Returns the bonus in $...."""
        return self.salary * self.bonus / 100

    def get_salary(self):
        """Returns the total salary in $...."""
        return self.salary + self.get_bonus()

    @staticmethod
    def create_bank_card(number):
        """Returns the bank card number of the employee...."""
        while True:
            card = ''.join([str(random.randint(0, 9)) for _ in range(number)])
            if card[0] != '0':
                break
        return card

    def write_employee_in_db(self, path):
        """Writes information about an employee to the database( .txt file)...."""
        with open(path, 'a') as file:
            file.write(f"Employee: {self.name}\n"
                       f"UUID: {self.create_id()}\n"
                       f"Position: {self.position}\n"
                       f"Level: {self.level}\n"
                       f"Department: {self.department}\n"
                       f"{company.name} login time: {datetime.datetime.now()}\n"
                       f"Working hours: {self.working_hours}\n"
                       f"{company.name} exit time: {self.get_exit_time()}\n"
                       f"Financial data of {self.name} ->\n"
                       f"Salary: {self.salary}$\n"
                       f"Income with the bonus: {self.get_salary()}$\n"
                       f"Bank information of {self.name} ->\n"
                       f"ID account: {self.create_bank_account()[0]}\n"
                       f"Checking account: {self.create_bank_account()[1]}\n"
                       f"Bank card number: {self.create_bank_card(16)}\n\n")

    def write_information_for_checkpoint(self):
        """Records information about an employee at the checkpoint( .txt file)...."""
        with open('checkpoint.txt', 'a') as file_checkpoint:
            file_checkpoint.write(f"Employee: {self.name}\n"
                                  f"UUID: {self.create_id()}\n"
                                  f"Position: {self.position}\n"
                                  f"Department: {self.department}\n"
                                  f"{company.name} login time: {datetime.datetime.now()}\n"
                                  f"Working hours: {self.working_hours}\n"
                                  f"Approximate {company.name} exit time: {self.get_exit_time()}\n\n")
        print(f"->  {self.name} was registered at the checkpoint\n")


class Subordinate(Person):
    """Subordinate class of the Person...."""

    def __init__(self, name, position, level, department, working_hours,
                 salary, bonus, projects, started_to_work):
        """Initializes the Subordinate class ...."""
        super().__init__(name, position, level, department, working_hours,
                         salary, bonus, id_employee=None, bank_account=None, bank_card=None)
        self.projects = projects
        self.started_to_work = started_to_work

    def get_projects(self):
        """Returns the projects of the employee...."""
        return self.projects

    def get_profit_form_the_project(self):
        """Returns the profit from the project...."""
        total_bonus = len(self.projects) * self.bonus
        bonus_for_project = self.salary * total_bonus / 100
        return self.salary + bonus_for_project

    def get_experience(self):
        """Returns the experience of the employee...."""
        return datetime.datetime.now().year - self.started_to_work

    def write_latest_data(self):
        """Writes the last data of the subordinate...."""
        with open('data_of_employees.txt', 'a') as file_last_data:
            file_last_data.write(f"\nLatest data of {self.name} ->\n"
                                 f"Level: {self.level}\n"
                                 f"Position: {self.position}\n"
                                 f"Experience: {self.get_experience()} years\n")
            for project in self.projects:
                file_last_data.write(f"Project: {project}\n"
                                     f"Profit from the project: {self.get_profit_form_the_project()}$\n")


class Supervisor(Person):

    def __init__(self, name, position, level, department, working_hours,
                 salary, bonus, places_of_work, term):
        """Initializes the Subordinate class ...."""
        super().__init__(name, position, level, department, working_hours,
                         salary, bonus, id_employee=None, bank_account=None, bank_card=None)
        self.places_of_work = places_of_work
        self.term = term

    def get_places_of_work(self):
        """Returns the places of work of the employee...."""
        return self.places_of_work

    @staticmethod
    def get_term_of_work():
        """Returns the term of work of the employee...."""
        return random.randint(1, 10)

    def write_last_data(self):
        """Writes the last data of the supervisor...."""
        with open('data_of_employees.txt', 'a') as file_last_data:
            file_last_data.write(f"\nData of {self.name} ->\n"
                                 f"Level: {self.level}\n"
                                 f"Position: {self.position}\n")
            for place in self.places_of_work:
                file_last_data.write(f"Place of work: {place}\n"
                                     f"Term of work: {self.get_term_of_work()} years\n")


class Company:

    def __init__(self, name):
        """Initializes the Company class...."""
        self.name = name.title()
        self.subordinates = []
        self.supervisors = []
        self.list_uuid = []
        self.visitors = []

    def add_subordinate(self, subordinate):
        """Adds the subordinate to the company...."""
        print(f"->  Subordinate: {subordinate.name} was added to the company {self.name}")
        return self.subordinates.append(subordinate)

    def add_supervisor(self, supervisor):
        """Adds the supervisor to the company...."""
        print(f"->  Supervisor: {supervisor.name} was added to the company {self.name}")
        return self.supervisors.append(supervisor)

    def add_uuid(self, number):
        """Adds the uuid to the employee in DB...."""
        print(f"->  Employee UUID was created and added to the database of the company {self.name}")
        return self.list_uuid.append(number)

    def add_visitor(self, visitor):
        """Adds the visitor to the DB "Visitors of Company"...."""
        print(f"->  Visitor: {visitor.name} was added to the database 'Visitors of {self.name}'")
        return self.visitors.append(visitor)

    def show_employees(self):
        """Shows all employees of the company...."""
        print(f"->  Employees of {self.name}:")
        for subordinate in self.subordinates:
            print(f"  Subordinate: {subordinate.name}")
        for supervisor in self.supervisors:
            print(f"  Supervisor: {supervisor.name}")

    def show_visitors(self):
        """Shows all visitors of the company...."""
        print(f"->  Visitors of {self.name}:")
        for visitor in self.visitors:
            print(f"  Visitor: {visitor.name}")

    def register_visitor_at_the_checkpoint(self, person):
        """Registers the visitor at the checkpoint...."""
        with open('checkpoint.txt', 'a') as file_checkpoint:
            file_checkpoint.write(f"Visitor: {person.name}\n"
                                  f"Meeting curator: {random.choice(self.supervisors).name}\n"
                                  f"Position: {person.position}\n"
                                  f"Level: {person.level}\n"
                                  f"Department: {person.department}\n"
                                  f"{company.name} login time: {datetime.datetime.now()}\n"
                                  f"Approximate {company.name} exit time: {datetime.datetime.now() + datetime.timedelta(minutes=20)}\n\n")
        print(f"->  {person.name} was registered at the checkpoint\n")

    def scan_pass_card(self, person):
        """Scans the pass-card of the employee...."""
        if person not in self.subordinates + self.supervisors + self.visitors:
            print(f"->  Pass-card of {person.name} was scanned.... > FAILED\n"
                  f"->  WARNING!!! {person.name} is DENIED ENTRY to company {self.name}\n")
        elif person in self.visitors:
            self.register_visitor_at_the_checkpoint(person)
            print(f"->  {person.name} > candidate for the position of 'Trainee'\n"
                  f"->  {person.name} scheduled interview {datetime.datetime.now() + datetime.timedelta(hours=2)}\n"
                  f"->  Company meeting curator: {random.choice(self.supervisors).name}\n")
        else:
            if person in self.subordinates:
                person.write_employee_in_db('subordinate.txt')
                delay_time()
                person.write_information_for_checkpoint()
                delay_time()
                person.write_latest_data()
            elif person in self.supervisors:
                person.write_employee_in_db('supervisor.txt')
                delay_time()
                person.write_information_for_checkpoint()
                delay_time()
                person.write_last_data()
            print(f"->  Pass-card of {person.name} was scanned.... > SUCCESSFULLY\n"
                  f"->  {person.name} is ALLOWED ENTRY to the company {self.name}\n")

    def run_elevator(self, person):
        """We go up to the desired floor...."""
        while True:
            if 5 <= int(input(f"->  {person.name} enter the floor you need: ")) <= 22:
                if person in self.subordinates + self.supervisors:
                    assert person.create_id() in self.list_uuid, f"->  UUID {person.name} is not found\n"
                    print(f"->  {person.name} REQUEST IS APPROVED\n")
                    break
                elif person in self.visitors:
                    print(f"->  {person.name} REQUEST IS APPROVED\n"
                          f"->  {person.name} please wait for your meeting supervisor\n")
                    break
                else:
                    print(f"->  {person.name} REQUEST IS DENIED\n")
                    break
            else:
                print(f"->  {person.name} you have entered a floor that does not belong to {self.name}.\n"
                      f"->  Please try again\n")

    @staticmethod
    def get_info_employees(category):
        """->  Returns the information about the employee...."""
        if category == 'subordinate':
            with open('subordinate.txt', 'r') as file_subordinate:
                return file_subordinate.read()
        elif category == 'supervisor':
            with open('supervisor.txt', 'r') as file_supervisor:
                return file_supervisor.read()
        else:
            return f"->  ERROR!!! The category {category} is not found\n"

    @staticmethod
    def get_info_checkpoint():
        """->  Returns the information with checkpoint of the company...."""
        with open('checkpoint.txt', 'r') as file_checkpoint:
            return file_checkpoint.read()

    @staticmethod
    def get_latest_data_of_employee():
        """->  Returns the latest data of employees...."""
        with open('data_of_employees.txt', 'r') as latest_data:
            return latest_data.read()

    def run(self, person):
        """->  Run the program...."""
        if person not in self.subordinates + self.supervisors + self.visitors:
            print(f"->  {person.say()}"
                  f"->  Pass-card of {person.name} was scanned.... > FAILED\n"
                  f"->  WARNING!!! {person.name} is DENIED ENTRY to company {self.name}\n"
                  f"->  {person.name} is not an employee of company {self.name}\n")
        else:
            return f"{delay_time()}" \
                   f"{print(company.run.__doc__)}\n" \
                   f"{delay_time()}" \
                   f"{person.say()}\n" \
                   f"{delay_time()}" \
                   f"{company.scan_pass_card(person)}\n" \
                   f"{delay_time()}" \
                   f"{company.run_elevator(person)}\n" \



company = Company("limelight networks")
user1 = Subordinate('daria veresha', 'tester', 'junior', 'it', 10,
                    1000, 15,
                    ['Selenium', 'Pytest'], 2019)
user2 = Supervisor('alex litvinov', 'QA Engineer', 'senior', 'it',
                   7, 12000, 65, ['Epam', 'Google'], 5)
user3 = Person("jon smith", "back-end", "trainee", 'it')
user4 = Person("john doe", "front-end", "trainee", 'it')


company.add_subordinate(user1)
delay_time()
company.add_supervisor(user2)
delay_time()
company.add_visitor(user3)
delay_time()
company.add_uuid(user1.create_id())
delay_time()
company.add_uuid(user2.create_id())
print('-------------------------------------------')
delay_time()
company.show_employees()
print('-------------------------------------------')
delay_time()
company.show_visitors()
print('-------------------------------------------')
company.run(user1)
print('-------------------------------------------')
company.run(user2)
print('-------------------------------------------')
company.run(user3)
print('-------------------------------------------')
delay_time()
company.run(user4)
print('-------------------------------------------')
delay_time()
print(company.get_info_employees.__doc__)
delay_time()
print(company.get_info_employees('subordinate'))
print('-------------------------------------------')
delay_time()
print(company.get_info_employees.__doc__)
delay_time()
print(company.get_info_employees('supervisor'))
print('-------------------------------------------')
delay_time()
print(company.get_info_checkpoint.__doc__)
delay_time()
print(company.get_info_checkpoint())
print('-------------------------------------------')
delay_time()
print(company.get_latest_data_of_employee.__doc__)
delay_time()
print(company.get_latest_data_of_employee())
print('-------------------------------------------')
