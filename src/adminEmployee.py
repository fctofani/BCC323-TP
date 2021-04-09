import globalContent

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

    def deleteEmployee(self, id):
        for i in globalContent.database.employeeContainer:
            if i.id == id:
                globalContent.database.employeeContainer.remove(i)
        
    def searchEmployee(self, id):
        for i in globalContent.database.employeeContainer:
            if i.id == id:
                return i
        
    def updateEmployee(self,
        employee, first_name="", last_name="", id=-1 ):
        
        for i in globalContent.database.employeeContainer:
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
    def listEmployees(self):
        print("\n------Lista de funcionários-------\n")
        idx = 1
        for i in globalContent.database.employeeContainer:
            print('('+str(idx)+')' + str(i))
            idx = idx + 1

        
    
        
    def createItem(self, item_name, id_item, value, description, status):
        item = Items(id_item, item_name, value, description, status)
        return item
        
    def deleteItem(self, itemsContainer, id_item):
        for i in itemsContainer:
            if i.id_item == id_item:
                if i.status == 'rented':
                    print("Não é possivel remover")
                else:
                    itemsContainer.remove(i)
        
    def showMenu(self):
        while(True):
            option = input('\n----- MENU ADMIN ----- \n'
                            + '(1) - Itens\n'
                            + '(2) - Clientes\n'
                            + '(3) - Funcionários\n'
                            + '(4) - SAIR\n')

            if(option == '1'): self.showMenuItems()
            elif(option == '2') : self.showMenuClients()
            elif(option == '3') : self.showMenuEmployees()
            elif(option == '4') : break
    
    def showMenuEmployees(self):
        while(True):
            option = input('----- MENU ITENS ----- \n'
                            + '(1) - Listar Funcionários\n'
                            + '(2) - Adicionar Funcionário\n'
                            + '(3) - Editar Funcionário\n'
                            + '(4) - Remover Funcionário\n'
                            + '(5) - SAIR\n')
            
            if(option == '1'): self.listEmployees()
            elif(option == '2'): print('Ainda não desenvolvido totalmente.')
            elif(option == '3'): print('Ainda não desenvolvido totalmente.')
            elif(option == '4'): print('Ainda não desenvolvido totalmente.')
            elif(option == '5'): break
    

    
