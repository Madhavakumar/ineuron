# 1. Create a function in python to read the text file and replace specific content of the file.
import logging,os

def read_replace(doc_name,content,replace_word=''):
    path = os.path.dirname(__file__)
    logging.basicConfig(filename=f"{doc_name.split('.')[0]}.log", format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',filemode='w',level=logging.DEBUG) 
    logger=logging.getLogger()

    # read input file 
    logger.info(f'{doc_name} file is reading!!!')
    file = open(path+'/'+doc_name,'rt')
    
    #read lines in the document 
    data = file.read()
    logger.info(f"{doc_name} opened in read mode")

    # replace the matching content 
    data = data.replace(content,replace_word)
    logger.info(f'{content} replaced as {replace_word}')

    # close the file after reading 
    file.close() 

    # open same file using write mode 
    file = open(path+'/'+doc_name,'wt')
    logger.info(f"{doc_name} opened in write mode")


    #overwrite the data replaced
    file.write(data)
    logger.info(f"{doc_name} wrote")


    #close the file
    file.close()
    logger.info(f"{doc_name} closed")

    return f"{doc_name} replacement Done"

# print(read_replace('example.txt','placement','screening'))



#2. Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.

"Abstract means blueprint of the particular class or function."

# BASCI OVERVIEW
from abc import ABC
class AbstarctClass(ABC):
    pass
# above the simple example for creating abstract class.

from abc import ABC, abstractmethod


class AbstractClassName(ABC):
    @abstractmethod
    def abstract_method_name(self):
        pass
# above is the simple exapmle for abstract class method creation.


# Real Example 

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # we are leaving this as a abstract class
    @abstractmethod
    def get_salary(self):
        pass
        # return float(self.salary)

# Multiple Inhertance
'''
inherit from multiple class, that means we are able access the function and attribute of the parent class inside the inherited child class
'''
# here we are inherit the Employee class from FulltimeEmployee class
class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary) # for defining the employee class constructor
        # self.salary = salary

    def get_salary(self): # function override from using the above abstract method
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name, salary=0) # for defining the employee class constructor
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self): # function override
        return self.worked_hours * self.rate

# main class function
class Payroll:
    def __init__(self):
        self.employee_list = []
        self.table_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            self.table_list.append([e.full_name,e.get_salary()])
            print(f"{e.full_name} \t ${e.get_salary()}")
    
    def print_table(self):
        from prettytable import PrettyTable
        table = PrettyTable(['Name','Salary'])
        for e in self.table_list:
            table.add_row(e)
        print(table)


payroll = Payroll()

payroll.add(FulltimeEmployee('John', 'Doe', 6000))
payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

payroll.print()

payroll.print_table()
