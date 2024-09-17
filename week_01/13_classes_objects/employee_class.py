# (CORE) DEVELOPER MINDSET

class Employee:

    # Class variables
    empCount = 0

    # Constructor and Data Intialization
    def __init__(self, n, company, salary):
        self.name = n
        self.company = company
        self.salary = salary
        self.tax = 0
        Employee.empCount += 1

    # Functions
    def printinfo(self):
        #self.v = 45
        #temp = 78
        print(self.name.upper())
        print("Object reference: ", self)
        print('-'*30)
        print('COMPANY    :', self.company)
        print('SALARY     :', self.salary)
        print('TAX        :', self.tax)
        print('\n\n')

    def setsalary(self, newsalary):
        self.x = 0
        self.salary = newsalary
        self.calctax()

    def getsalary(self):
        return self.salary

    def calctax(self):
        self.tax = 0.1 * float(self.salary.split()[0])


# ------------------------------------------------------------------

# USER/APP DEVELOPER

e = Employee('Anil', 'Publis-Sapient', '10000000 USD')
e.printinfo()

e.calctax()
e.printinfo()

e.setsalary('200000 USD')
e.printinfo()