''' '''
from adminEmployee import AdminEmployee
from commonEmployee import CommonEmployee
from client import Client
from items import Items


class System:
    def __init__(self):
        self.admin = AdminEmployee(first_name="Seu Tião", last_name="Meireles", id=0, system = self)
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
        self.employeeContainer.append(self.admin.createCommonEmployee(
            first_name = "Lucas",last_name =  "Natali", id = 990, system = self
        ))
        self.employeeContainer.append(self.admin.createCommonEmployee(
            first_name = "Geraldo", last_name = "Azevedo", id = 992, system = self
        ))
        self.employeeContainer.append(self.admin.createCommonEmployee(
            first_name = "Ademir",last_name =  "edivaldo", id = 993, system = self
        ))
        self.employeeContainer.append(self.admin.createCommonEmployee(
            first_name = "marlon", last_name = "ponei", id =994, system = self
        ))

        '''Create Clients by Admin'''
        #Insert client 1
        self.clientContainer.append(self.admin.createClient(
            "Erika", "Oliveira",
            "888.225.763-72",
            "erika@email.com",
            "kkk8988"
        ))
        #Insert client 2
        self.clientContainer.append(self.admin.createClient(
            "Oswaldo", "Wiks",
            "992.888.111-82",
            "oswaldin@email.com",
            "xia"
        ))
        #Insert client 3 
        self.clientContainer.append(self.admin.createClient(
            "Janaina", "Kristakens",
            "878.008.112-66",
            "janaina@email.com",
            "jana2222"
         ))

        self.clientContainer.append(self.admin.createClient(
            "Nicolas", "Oliveira",
            "888.288.223-72",
            "nicolas@email.com",
            "k--k"
        ))  #Insert client 4
        self.clientContainer.append(self.admin.createClient(
            "Mirella", "Wiks",
            "992.002.111-22",
            "mirella@email.com",
            "banana"
        )) #Insert client 5

        self.clientContainer.append(self.admin.createClient(
            "Eustaquio", "Kristakens",
            "118.008.212-66",
            "eustaquio@email.com",
            "sonho"
         ))  #Insert client 6
        
    def generateItems(self):
        self.itemsContainer.append(self.admin.createItem(
            item_name= "item1",
            id_item=1,
            value = 20,
            description="item top",
            status = "available"
        ))
        self.itemsContainer.append(self.admin.createItem(
            item_name= "item2",
            id_item=2,
            value = 50,
            description="item fera",
            status = "available"
        ))
        self.itemsContainer.append(self.admin.createItem(
            item_name= "item3",
            id_item=3,
            value = 990,
            description="item caro",
            status = "available"
        ))
        self.itemsContainer.append(self.admin.createItem(
            item_name= "item4",
            id_item=4,
            value = 110.5,
            description="item show",
            status = "available"
        ))

        
        
  
    def run(self):
        self.running = True
        while(self.running):
            option = input('----- LOGIN ----- \n'
                        + '(1) - Admin\n'
                        + '(2) - Funcionário\n')

            if(option == "1"):
                self.userLogged = self.admin;
                self.userLogged.showMenu()
            else:
                self.admin.listEmployees()
                func = input('Qual funcionário você é?')
                self.userLogged = self.employeeContainer[int(func)-1]
                self.userLogged.showMenu()

       

        # self.admin.listEmployees(employees=self.employeeContainer)
        # self.admin.listClients(clients=self.clientContainer)

        # print("----------------------------------------")
        # print("Buscando um cliente através do admin: ", self.admin.searchClient(
        #     clientContainer = self.clientContainer,
        #     cpf="992.002.111-22"
        # ), "\n")
        # print("Buscando um cliente através do funcionario comum: ", self.commonEmp.searchClient(
        #     clientContainer = self.clientContainer,
        #     cpf="118.008.212-66"
        # ), "\n")
        # print("--------------------------------------")

        # print("Deletando o cliente de cpf {} através do admin:  ".format("118.008.212-66"))
        # self.admin.deleteClient(
        #         clientContainer=self.clientContainer,
        #         cpf = "118.008.212-66")

        # print("\nDeletando o cliente de cpf {} através do funcionário comum".format("992.002.111-22"))
        # self.commonEmp.deleteClient(
        #     clientContainer=self.clientContainer,
        #     cpf = "992.002.111-22"
        # )

        # self.admin.listClients(clients=self.clientContainer)

        # print("Atualizando o cliente de cpf {} através do admin".format("888.225.763-72"))
        # cli = self.admin.searchClient(self.clientContainer, "888.225.763-72")
        # self.admin.updateClient(
        #     clientContainer=self.clientContainer,
        #     client = cli,
        #     last_name="arrombada"
        # )
        # print("Atualizando o cliente de cpf {} através do admin".format("992.888.111-82"))
        # cli = self.admin.searchClient(self.clientContainer, "992.888.111-82")
        # self.admin.updateClient(
        #     clientContainer=self.clientContainer,
        #     client = cli,
        #     last_name = "Dias",
        #     cpf = "123.456.789-10"
        # )

        # self.admin.listClients(clients=self.clientContainer)

        # print("Deletando o funcionário de matricula {}:  ".format(990))
        # self.admin.deleteEmployee(
        #         employeeContainer=self.employeeContainer,
        #         id=990
        # )

        # print("\nDeletando o funcionario de matricula {} ".format(992))
        # self.admin.deleteEmployee(
        #     employeeContainer=self.employeeContainer,
        #     id = 992
        # )
        # print("\n Atualizando funcionário de matricula {}".format(993))
        # emp = self.admin.searchEmployee(self.employeeContainer, 993)
        # self.admin.updateEmployee(
        #     employeeContainer= self.employeeContainer,
        #     employee = emp,
        #     first_name="Mirosmar",
        #     last_name="Klose"
        # )
        # self.admin.listEmployees(self.employeeContainer)


        


        
    