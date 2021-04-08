import globalContent

from employee import Employee
class CommonEmployee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    

    def __str__(self):
        return "First Name: {}, Last Name: {}, ID: {} ".format(
            self.first_name, self.last_name, self.id
        )
    
    def showMenu(self):
        while(True):
            option = input('\n----- MENU FUNCIONÁRIO ----- \n'
                            + '(1) - Itens\n'
                            + '(2) - Clientes\n'
                            + '(3) - SAIR\n')
            if(option == '1'): self.showMenuItems()
            elif(option == '2'): self.showMenuClients()
            elif(option == '3'): break


                
    