from employee import Employee
class CommonEmployee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    

    def __str__(self):
        return "First Name: {}, Last Name: {}, ID: {} ".format(
            self.first_name, self.last_name, self.id
        )
    
