''' '''
from adminEmployee import AdminEmployee
from commonEmployee import CommonEmployee
from client import Client
from item import Item


class System:
    def __init__(self):
        self.itemsContainer = []
        self.clientContainer = []
        self.employeeContainer = []
        self.userLogged = None
        self.running = False
        
    def initializeContent(self):
        self.itemsContainer.append(Item('Titanic', '18.50', 'Um artista pobre e uma jovem rica se conhecem e se apaixonam na fatídica jornada do Titanic, em 1912.'))
        self.itemsContainer.append(Item('Na Natureza Selvagem', '25.25', 'Christopher McCandless, filho de pais ricos, se forma na universidade de Emory como um dos melhores estudantes e atletas. Porém, em vez de em embarcar em uma carreira prestigiosa e lucrativa, ele escolhe doar suas economias para caridade, livrar-se de seus pertences e viajar pelo Alasca.'))
        self.itemsContainer.append(Item('Missão Impossível', '13.25', 'O agente do governo Ethan Hunt e seu mentor, Jim Phelps, embarcam em uma missão secreta que toma um rumo desastroso, na qual Jim é morto e Ethan torna-se o principal suspeito do assassinato.'))
        self.itemsContainer.append(Item('Tarzan', '8.70', 'Um bebê perde os pais na selva. Órfão e sozinho, ele é encontrado por uma macaca que o cria como se fosse seu próprio filho.'))
        self.itemsContainer.append(Item('Spirit', '11.50', 'Animação sobre a amizade entre um menino indígena e um cavalo indomável apaixonado por uma égua. Ambientada no Velho Oeste americano, mostra o impacto do processo civilizatório na vida dos três e também na amizade que construíram.'))

        self.clientContainer.append(Client('Lucca', 'Martins', '85123422-24', 'lucca.martins@aluno.ufop.edu.br', '(35) 99995-4661'))
        self.clientContainer.append(Client('Jackie', 'Lee', '621354321-13', 'lee.jackie@gmail.com', '(11) 99953-3931'))
        self.clientContainer.append(Client('Olívia', 'Cabral', '512345564-62', 'olivia.bh@gmail.com', '(31) 98736-9625'))

        self.employeeContainer.append(AdminEmployee('Seu Tião', 'Meireles'))
        self.employeeContainer.append(CommonEmployee('Juliana', 'Souza', '2900.45'))
        self.employeeContainer.append(CommonEmployee('Paulo', 'Vicente', '1450.56'))
        self.employeeContainer.append(CommonEmployee('Rafaela', 'Parreira', '1890.00'))

    def run(self):
        self.initializeContent()
        self.login()        

        # self.employeeContainer.append(AdminEmployee('Josué', 'Oliveira', '1'))
        # self.itemsContainer.append(Items("duro de matar", '12',5,'bom demais né gente','available'))
        # self.clientContainer.append(Client('Ezequiel', 'Cunha', 'ezequiel@gmail.com', '83892993949', '(31)999546842'))
        # print('vai chamar')
        # self.employeeContainer[0].rent(self.itemsContainer[0], self.clientContainer[0])
        # print(self.itemsContainer[0].status)


    def login(self):
        print("\n\n------ LOGIN ------\n\n")
        print("(1) - Administrador")
        print("(2) - Funcionário")
        print("(3) - SAIR\n" )

        self.login = input()
        
        if(self.login == '1'): 
            print('\n------ Qual administrador você é? ------')
            idx = 1 
            for admin in filter(lambda x: (x.role == 'Admin'), self.employeeContainer):
                print('(' + str(idx) + ') - ' + admin.first_name + ' ' + admin.last_name)
                idx = idx + 1
            chosenAdminIdx = input()

            self.userLogged = self.employeeContainer[int(chosenAdminIdx) - 1]

            self.running = True
            self.showMainMenu()
        elif(self.login == '2'):
            print('\n------ Qual funcionário você é? ------')
            idx = 1 
            for common in filter(lambda x: (x.role == 'Common'), self.employeeContainer):
                print('(' + str(idx) + ') - ' + common.first_name + ' ' + common.last_name)
                idx = idx + 1
            chosenCommonIdx = input()

            self.userLogged = self.employeeContainer[int(chosenCommonIdx) - 1]

            self.running = True
            self.showMainMenu()
        elif(self.login == '3'):
            self.running = False
            print('Sistema finalizado.')
        else:
            print('Opção inválida.')
            
    def showMainMenu(self):
        while(self.running):
            if(self.login == '1'):
                option = input("\n\n------ MENU ADMIN ------\n\n" +
                                "(1) - Itens\n(2) - Clientes\n(3) - Funcionários\n(4) - Relatórios\n(5) - SAIR\n")
                
                if(option == '1'): self.showMenuItems()
                elif(option == '2'): self.showMenuCustomers()
                elif(option == '3'): self.showMenuEmployees()
                elif(option == '4'): self.showMenuReports()
                elif(option == '5'): 
                    self.running = False
                    print('Sistema finalizado.')

            elif(self.login == '2'):
                option = input("\n\n------ MENU FUNCIONÁRIO ------\n\n" +
                                "(1) - Alugar Item\n(2) - Clientes\n(3) - SAIR\n")
                
                if(option == '1'): self.userLogged.rentItem(self)
                elif(option == '2'): self.showMenuCustomers()
                elif(option == '3'): 
                    self.running = False
                    print('Sistema finalizado.')

        
    def showMenuItems(self):
        option = input("\n\n------ MENU ITEMS ------\n\n" +
                        "(1) - Listar Itens\n(2) - Cadastrar Itens\n(3) - Alugar Item\n(4) - SAIR\n")

        if(option == '1'): self.listItems()
        elif(option == '2'): self.userLogged.createItem(self)
        elif(option == '3'): self.userLogged.rentItem(self)
        elif(option == '4'): self.showMainMenu()
    
    def listItems(self):
        print('\n\n------ LISTA DE ITENS ------\n')
        idx = 1
        for item in self.itemsContainer:
            print('\nITEM ' + str(idx))
            item.print()
            idx = idx + 1
    
   

  