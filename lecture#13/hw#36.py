"""
Task 36. Company`s Checkpoint
Description:
The essence of this project is this: we have a checkpoint of a company that is located in a business
center, it is allocated a certain number of floors and this is (the Hall where there are a number of
turnstiles lined up, the main entrance to the company is an elevator, which can only be called by
scanning an employee’s pass, a monitor and person (company security service) behind the monitor)
The program works as follows:
1. A person (current employee) enters the company lobby, approaches the turnstile and scans his pass card,
after which the system checks the person’s first and last name in the company database, if there is one
- the turnstile opens and the employee goes to the elevator to go up the floor he needs.
2. The employee calls the elevator by scanning his pass card, then the system asks the employee for
the floor number where he wants to arrive.
3. The employee enters his request (floor number) on the monitor. The system again checks the employee’s
first and last name in the company database, and the 2nd level of verification also comes into force
- the system checks the employee’s yuuid for his presence in the company database. If there is one, the
system approves the employee’s request and the elevator moves to the floor specified by the employee.
4. At the request of the company's security service, more detailed information, financial data or the
latest work data can be obtained for any employee.
5. If a person is not in the company’s database as a subordinate or manager or visitor (in this case,
the system contacts the HR department and assigns him support from among the managers), then at the first
level of verification the system issues a warning about this and asks the non-working person to contact
the company’s Security Service or the appropriate person who made the appointment for him.
"""
import time
import uuid
import datetime
import random


def delay_time():
    time.sleep(3)


class Person:

    def __init__(self, name, position, level, department, working_hours,
                 id_employee=None, bank_info=None, **kwargs):
        """Initializes the Person class...."""
        self.name = name.title()
        self.position = position.title()
        self.level = level.capitalize()
        self.department = department.upper()
        self.__uuid = id_employee
        self.working_hours = working_hours
        self.bank_info = bank_info
        self.kwargs = kwargs

    def say(self):
        """Person says...."""
        print(f"{self.name} says: > Hi, I`m a {self.position} from {self.department} departament.\n")

    def get_id(self):
        """Returns the employee identifier in uuid format...."""
        if self.__uuid is not None:
            return self.__uuid
        else:
            self.__uuid = uuid.uuid4()
            return self.__uuid

    def get_time_exit(self):
        """Returns the time the employee left work...."""
        return datetime.datetime.now() + datetime.timedelta(hours=self.working_hours)

    def get_bank_information(self):
        """Returns the bank information of the employee...."""
        if self.bank_info is not None:
            return self.bank_info
        else:
            self.bank_info = [
                uuid.uuid4(),
                random.randint(1000000, 1000000000)
            ]
            return self.bank_info


class Subordinate(Person):
    """Subordinate class of the Person...."""

    def __init__(self, name, position, level, department, working_hours, **kwargs):
        """Initializes the Subordinate class ...."""
        super().__init__(name, position, level, department, working_hours,
                         id_employee=None, bank_info=None, **kwargs)

    def get_projects(self):
        """Returns the names of all projects...."""
        return self.kwargs.get('project', 'No key <projects>')

    def get_bonus(self):
        """Returns the bonus in $...."""
        result = []
        for item in self.kwargs['percent_bonus']:
            res = self.kwargs['salary'] * item / 100
            result.append(res)
        return sum(result)

    def get_salary(self):
        """Returns the total salary in $...."""
        return self.kwargs['salary'] + self.get_bonus()

    def write_information(self):
        """Writes information of the subordinate to a .txt file"""
        with open('subordinate.txt', 'a') as file_subordinate:
            file_subordinate.write(f"Subordinate: {self.name}\n"
                                   f"ID: {self.get_id()}\n"
                                   f"Position: {self.position}\n"
                                   f"Level: {self.level}\n"
                                   f"Department: {self.department}\n"
                                   f"Time of entry to work: {datetime.datetime.now()}\n"
                                   f"Working hours: {self.working_hours}\n"
                                   f"Time of exit from work: {self.get_time_exit()}\n"
                                   f"Financial data of {self.name} ->\n"
                                   f"Salary: {self.kwargs['salary']}$\n"
                                   f"Percent of the salary in $: {self.get_bonus()}$\n"
                                   f"Income with bonus: {self.get_salary()}$\n"
                                   f"Bank information of {self.name} ->\n"
                                   f"ID account: {self.get_bank_information()[0]}\n"
                                   f"Checking account: {self.get_bank_information()[1]}\n"
                                   f"His/Her projects: {self.get_projects()}\n"
                                   f"Last data of {self.name}: ->\n"
                                   f"Last his/her project: {self.kwargs['project'][-1]}\n\n")
        with open('checkpoint.txt', 'a') as file_checkpoint:
            file_checkpoint.write(f"Subordinate: {self.name}\n"
                                  f"ID: {self.get_id()}\n"
                                  f"Position: {self.position}\n"
                                  f"Department: {self.department}\n"
                                  f"Time of entry to work: {datetime.datetime.now()}\n"
                                  f"Working hours: {self.working_hours}\n"
                                  f"Time of exit from work: {self.get_time_exit()}\n\n")
        print(f"->  Information about {self.name} was successfully written to the file subordinate.txt")


class Supervisor(Person):

    def __init__(self, name, position, level, department, working_hours, **kwargs):
        """Initializes the Supervisor class ...."""
        super().__init__(name, position, level, department, working_hours,
                         id_employee=None, bank_info=None, **kwargs)

    def get_percent(self):
        """Returns the percent in $...."""
        return self.kwargs['salary'] * self.kwargs['rating'] / 100

    def get_salary(self):
        """Returns the salary in $...."""
        return self.kwargs['salary'] + self.get_percent()

    def write_information(self):
        """Writes information of the supervisor to a .txt file"""
        with open('supervisor.txt', 'a') as file_supervisor:
            file_supervisor.write(f"Supervisor: {self.name}\n"
                                  f"ID: {self.get_id()}\n"
                                  f"Position: {self.position}\n"
                                  f"Level: {self.level}\n"
                                  f"Department: {self.department}\n"
                                  f"Time of entry to work: {datetime.datetime.now()}\n"
                                  f"Working hours: {self.working_hours}\n"
                                  f"Time of exit from work: {self.get_time_exit()}\n"
                                  f"Financial data of {self.name} ->\n"
                                  f"Salary: {self.kwargs['salary']}$\n"
                                  f"Percent of the salary in $: {self.get_percent()}$\n"
                                  f"Income with bonus: {self.get_salary()}$\n"
                                  f"Bank information of {self.name} ->\n"
                                  f"ID account: {self.get_bank_information()[0]}\n"
                                  f"Checking account: {self.get_bank_information()[1]}\n"
                                  f"Last data of {self.name}: ->\n"
                                  f"Rating: {self.kwargs['rating']}\n"
                                  f"His/Her projects: {self.kwargs['project']}\n"
                                  f"Last his/her project: {self.kwargs['project'][-1]}\n\n")
        with open('checkpoint.txt', 'a') as file_checkpoint:
            file_checkpoint.write(f"Supervisor: {self.name}\n"
                                  f"ID: {self.get_id()}\n"
                                  f"Position: {self.position}\n"
                                  f"Department: {self.department}\n"
                                  f"Time of entry to work: {datetime.datetime.now()}\n"
                                  f"Working hours: {self.working_hours}\n"
                                  f"Time of exit from work: {self.get_time_exit()}\n\n")
        print(f"->  Information about {self.name} was successfully written to the file supervisor.txt")


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
        print(f"->  UUID was created and added to the database of the company {self.name}")
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

    def scan_pass_card(self, person):
        """Scans the pass-card of the employee...."""
        if person not in self.subordinates + self.supervisors + self.visitors:
            print(f"->  Pass-card of {person.name} was scanned.... > FAILED\n"
                  f"->  WARNING!!! {person.name} is DENIED ENTRY to company {self.name}\n")
        elif person in self.visitors:
            print(f"->  {person.name} > candidate for the position of 'Trainee'\n"
                  f"->  {person.name} scheduled interview {datetime.datetime.now() + datetime.timedelta(hours=2)}\n"
                  f"->  Company meeting curator: {random.choice(self.supervisors).name}\n")
            with open('checkpoint.txt', 'a') as file_checkpoint:
                file_checkpoint.write(f"Visitor: {person.name}\n"
                                      f"Meeting curator: {random.choice(self.supervisors).name}\n"
                                      f"Position: {person.position}\n"
                                      f"Level: {person.level}\n"
                                      f"Department: {person.department}\n"
                                      f"Time of entry to work: {datetime.datetime.now()}\n"
                                      f"Time of exit from work: {datetime.datetime.now() + datetime.timedelta(minutes=20)}\n\n")
        else:
            print(f"->  Pass-card of {person.name} was scanned.... > SUCCESSFULLY\n"
                  f"->  {person.name} is ALLOWED ENTRY to the company {self.name}\n")

    def run_elevator(self, person):
        """We go up to the desired floor...."""
        while True:
            if int(input(f"->  {person.name} enter the floor you need: ")) <= 22:
                if person in self.subordinates + self.supervisors:
                    for item in self.list_uuid:
                        assert isinstance(item, uuid.UUID), f"{person.name} -> Your ID is not class <UUID>!"
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

    def get_info_employee(self, person):
        """->  Returns the information about the employee...."""
        if person in self.subordinates:
            with open('subordinate.txt', 'r') as file_subordinate:
                return file_subordinate.read()
        elif person in self.supervisors:
            with open('supervisor.txt', 'r') as file_supervisor:
                return file_supervisor.read()
        else:
            return f"->  {person.name} does not work for company {self.name}"

    @staticmethod
    def get_info_checkpoint():
        """->  Returns the information with checkpoint of the company...."""
        with open('checkpoint.txt', 'r') as file_checkpoint:
            return file_checkpoint.read()

    def run(self, person):
        """->  Run the program...."""
        if person not in self.subordinates + self.supervisors + self.visitors:
            print(f"->  {person.say()}"
                  f"{delay_time()}"
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
user1 = Subordinate('daria veresha', 'tester', 'junior', 'it',
                    10, project=('Flask', 'Django', 'FastAPI'),
                    percent_bonus=(10, 20, 30), salary=1000)
user2 = Supervisor('alex litvinov', 'QA Engineer', 'senior', 'it',
                   7, project=('Flask', 'FastAPI', 'Django'),
                   rating=98.6, salary=12000)
user3 = Person("jon smith", "back-end", "trainee", 'it',
               None)
user4 = Person("john doe", "front-end", "trainee", 'it',
               None)

user1.write_information()
user2.write_information()
company.add_subordinate(user1)
company.add_supervisor(user2)
company.add_visitor(user3)
company.add_uuid(user1.get_id())
company.add_uuid(user2.get_id())
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
print(company.get_info_checkpoint.__doc__)
print(company.get_info_checkpoint())
print('-------------------------------------------')
delay_time()
print(company.get_info_employee.__doc__)
print(company.get_info_employee(user1))
print('-------------------------------------------')
delay_time()
print(company.get_info_employee.__doc__)
print(company.get_info_employee(user2))
print('-------------------------------------------')
delay_time()
print(company.get_info_employee.__doc__)
print(company.get_info_employee(user3))
