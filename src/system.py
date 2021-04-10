''' '''
from adminEmployee import AdminEmployee
from commonEmployee import CommonEmployee
from client import Client
from items import Items

class System:
    def __init__(self):
        self.admin = AdminEmployee(first_name="Seu Tião", last_name="Meireles", id=0)
        # self.commonEmp = CommonEmployee(first_name="", last_name="", id=0)
        self.userLogged = None
        self.itemsContainer = []
        self.clientContainer = []
        self.employeeContainer = []
        self.running = False
        
    def authentication(self, login, password):
        pass

    def generateClientAndEmployees(self):
        #Insert employees 
        self.employeeContainer.append(CommonEmployee(
            first_name = "Lucas",last_name =  "Natali", id = 990
        ))
        self.employeeContainer.append(CommonEmployee(
            first_name = "Geraldo", last_name = "Azevedo", id = 992
        ))
        self.employeeContainer.append(CommonEmployee(
            first_name = "Ademir",last_name =  "edivaldo", id = 993
        ))
        self.employeeContainer.append(CommonEmployee(
            first_name = "marlon", last_name = "ponei", id =994
        ))

        '''Create Clients by Admin'''
        #Insert client 1
        self.clientContainer.append(Client(
            "Erika", "Oliveira",
            "888.225.763-72",
            "erika@email.com",
            "kkk8988"
        ))
        #Insert client 2
        self.clientContainer.append(Client(
            "Oswaldo", "Wiks",
            "992.888.111-82",
            "oswaldin@email.com",
            "xia"
        ))
        #Insert client 3 
        self.clientContainer.append(Client(
            "Janaina", "Kristakens",
            "878.008.112-66",
            "janaina@email.com",
            "jana2222"
         ))

        self.clientContainer.append(Client(
            "Nicolas", "Oliveira",
            "888.288.223-72",
            "nicolas@email.com",
            "k--k"
        ))  #Insert client 4
        self.clientContainer.append(Client(
            "Mirella", "Wiks",
            "992.002.111-22",
            "mirella@email.com",
            "banana"
        )) #Insert client 5

        self.clientContainer.append(Client(
            "Eustaquio", "Kristakens",
            "118.008.212-66",
            "eustaquio@email.com",
            "sonho"
         ))  #Insert client 6
        
    def generateItems(self):
        self.itemsContainer.append(Items(
            "item1",
            1,
            20,
            "item top",
            "available"
        ))
        self.itemsContainer.append(Items(
            "item2",
            2,
            50,
            "item fera",
            "available"
        ))
        self.itemsContainer.append(Items(
            "item3",
            3,
            990,
            "item caro",
            "available"
        ))
        self.itemsContainer.append(Items(
            "item4",
            4,
            110.5,
            "item show",
            "available"
        ))

        
        
  
    def run(self):
        self.running = True
        while(self.running):
            option = input('----- LOGIN ----- \n'
                        + '(1) - Admin\n'
                        + '(2) - Funcionário\n'
                        + '(3) - Sair\n')

            if(option == "1"):
                self.userLogged = self.admin;
                self.userLogged.showMenu()
            elif(option == "2"):
                self.admin.listEmployees()
                func = input('Qual funcionário você é?')
                self.userLogged = self.employeeContainer[int(func)-1]
                self.userLogged.showMenu()
            else:
                quit()

       




        


        
    