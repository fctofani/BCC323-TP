from employee import Employee
from commonEmployee import CommonEmployee
from items import Items

class AdminEmployee(Employee):
    def __init__(self):
        super().__init__()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)        
        
    

    def createCommonEmployee(self, **kwargs):
        common = CommonEmployee(**kwargs)
        return common
    def createAdminEmployee(self, **kwargs):
        admin = AdminEmployee(**kwargs)
        return admin

    def deleteEmployee(self, employeeContainer, id):
        for i in employeeContainer:
            if i.id == id:
                employeeContainer.remove(i)
        
    def searchEmployee(self, employeeContainer, id):
        for i in employeeContainer:
            if i.id == id:
                return i
        
    def updateEmployee(self, employeeContainer,
        employee, first_name="", last_name="", id=-1 ):
        
        for i in employeeContainer:
            if i == employee:
                if first_name == "":
                    i.first_name = i.first_name
                else:
                    i.first_name = first_name
                if last_name == "":
                    i.last_name = i.last_name
                else:
                    i.last_name = last_name
                if id == -1:
                    i.id = i.id
                else:
                    i.id = id
    def listEmployees(self, employees):
        print("------Lista de funcionários-------")
        for i in employees:
            print(i)
        
    
        
    def createItem(self, item_name, id_item, value, description, status):
        item = Items(id_item, item_name, value, description, status)
        return item
        
    def deleteItem(self, itemsContainer, id_item):
        for i in itemsContainer:
            if i.id_item == id_item:
                itemsContainer.remove(i)
        
    



    
