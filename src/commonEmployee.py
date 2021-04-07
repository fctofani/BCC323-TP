from employee import Employee

class CommonEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        self.salary = salary
        super(CommonEmployee, self).__init__(first_name, last_name, 'Common')
        pass
    
   
