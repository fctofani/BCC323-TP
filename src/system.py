''' '''
from adminEmployee import AdminEmployee
from client import Client
from items import Items


class System:
    def __init__(self):
        self.itemsContainer = []
        self.clientContainer = []
        self.employeeContainer = []
        
    def authentication(self, login, password):
        pass

    def generateClientAndEmployees(self):
        self.clientContainer.append()
        
    def run(self):
        self.employeeContainer.append(AdminEmployee('Josué', 'Oliveira', '1'))
        self.itemsContainer.append(Items("duro de matar", '12',5,'bom demais né gente','available'))
        self.clientContainer.append(Client('Ezequiel', 'Cunha', 'ezequiel@gmail.com', '83892993949', '(31)999546842'))
        print('vai chamar')
        self.employeeContainer[0].rent(self.itemsContainer[0], self.clientContainer[0])
        print(self.itemsContainer[0].status)


        


        
    