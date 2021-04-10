from client import Client
import globalContent
class Employee:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.id = 1
    def __init__(self, **kwargs):
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.id = kwargs['id']

    def __str__(self):
        return "First Name: {}, Last Name: {}, ID: {}".format(
            self.first_name, self.last_name, self.id
        )
    

    def createClient(self, first_name, last_name, cpf, email,phone):
        client = Client(first_name, last_name, cpf, email,phone)
        globalContent.database.clientContainer.append(client)
        return client
        
    def searchClient(self, cpf):
        for i in globalContent.database.clientContainer:
            if i.cpf == cpf:
                return i
        print("cliente não encontrado")
        
    def deleteClient(self, cpf):
        for i in globalContent.database.clientContainer:
            if i.cpf == cpf:
                print(i.cpf)
                print(cpf)
                globalContent.database.clientContainer.remove(i)
                print("cliente removido")
                return True
        print("cliente não encontrado")             
        return False
        
    def updateClient(self, client, 
        first_name = "", last_name = "",
         cpf = "", email = "", phone = ""):
        for i in globalContent.database.clientContainer:
            if i == client:
                if(first_name == ""): i.first_name = i.first_name 
                else:
                    i.first_name = first_name
                if(last_name == ""): i.last_name = i.last_name 
                else: 
                    i.last_name = last_name
                if(cpf == ""): i.cpf = i.cpf 
                else: 
                    i.cpf = cpf
                if(email == ""): i.email = i.email 
                else: 
                    i.email = email
                if(phone == ""): i.phone = i.phone 
                else: 
                    i.phone = phone
              
    def listClients(self):
        print("\n----------Lista de clientes-------")
        idx = 1
        for i in globalContent.database.clientContainer:
            print('('+str(idx)+')' + str(i))
            idx = idx + 1
        

    def rent(self, item, client):
        if item.status == 'rented':
            #print('item já está alugado.')
            return False
        else:
            item.status = 'rented'
            #print("item alugado com sucesso")
            client.rentedItems.append(item) #status alugado
            return True

    def giveBack(self, client):
        if len(client.rentedItems) > 0:
            for i in client.rentedItems:
                i.status = 'available'
                client.rentedItems.remove(i)
                print(i.item_name + " devolvido")
        else:
            print("cliente não possui itens emprestados")

    def updateItem(self, item, item_name="", id_item=-1,
        value=-1, description="", status = ""
    ):
        for i in globalContent.database.itemsContainer:
            if i == item:
                if item_name == "": i.item_name = i.item_name
                else:
                    i.item_name = item_name
                if id_item == -1:
                    i.id_item = i.id_item
                else:
                    i.id_item = id_item
                if value == -1:
                    i.value = i.value
                else:
                    i.value = value
                if description == "":
                    i.description = i.description
                else:
                    i.description = description
                if status == "":
                    i.status = i.status
                else:
                    i.status = status

        
    def searchItem(self, id_item):
        for i in globalContent.database.itemsContainer:
            if i.id_item == id_item:
                return i
        
    def listItems(self):
        print('\n----- Lista de Itens -----\n')
        idx = 1
        for i in globalContent.database.itemsContainer:
            print('('+str(idx)+')' + str(i))
            idx = idx + 1
        
    def showMenuClients(self):
        while(True):
            option = input('\n----- MENU Clients ----- \n'
                            + '(1) - Listar Clientes\n'
                            + '(2) - Adicionar Cliente\n'
                            + '(3) - Editar Cliente\n'
                            + '(4) - Remover Cliente\n'
                            + '(5) - SAIR\n')
            
            if(option == '1'): self.listClients()
            elif(option == '2'):

                first_name = input("Primeiro nome: ")
                last_name = input("Ultimo nome:")
                cpf = input("CPF: ")
                email = input("Email: ")
                phone = input("Phone: ")
                cli = self.createClient(first_name, last_name, cpf, email, phone)
                globalContent.database.clientContainer.append(cli)
            elif(option == '3'):
                cpf = input("CPF do cliente que você deseja buscar: ")
                cli = self.searchClient(cpf)
                first_name = input("Primeiro nome: ")
                last_name = input("Ultimo nome: ")
                cpf = input("CPF: ")
                email = input("Email: ")
                phone = input("Phone: ")
                self.updateClient(cli, first_name, last_name, cpf, email, phone)
            elif(option == '4'):
                cpf = input("Digite o cpf do cliente a ser removido")
                self.deleteClient(cpf)

            elif(option == '5'): break

                name = input('digite o nome\n')
                lastName = input('ultimo nome\n')
                cpf = input('digite o cpf\n')
                phone = input('digite o telefone\n')
                email = input('digite o email\n')
                self.createClient(name, lastName, cpf, email, phone)
                self.listClients()
            elif(option == '3'): 
                searchcpf = input('degite o cpf\n')
                client = self.searchClient(searchcpf)

                if (client):
                    print("\n --- dados para editar: \n")
                    name = input('digite o nome\n')
                    lastName = input('ultimo nome\n')
                    cpf = input('digite o cpf\n')
                    phone = input('digite o telefone\n')
                    email = input('digite o email\n')

                    self.updateClient(client, name, lastName, cpf, phone, email)
                    self.listClients()
                else:
                    print("erro")
            elif(option == '4'): 
                cpf = input('digite o cpf\n')
                deleted = self.deleteClient(cpf)
                if deleted:
                    self.listClients()
                else:
                    print('erro ao remover cliente')
            else: 
                break


    def showMenuItems(self):
        while(True):
            option = input('\n----- MENU ITENS ----- \n'
                            + '(1) - Listar Itens\n'
                            + '(2) - Alugar Item\n'
                            + '(3) - Devolver Item\n'
                            + '(4) - Atualizar Item\n'
                            + '(5) - SAIR\n')

            if(option == '1'): self.listItems()
            elif(option == '2'):
                self.listItems()
                item = input('\nItem que será alugado: ')
                self.listClients()
                client = input('\nCliente a alugar: ')
                self.rent(globalContent.database.itemsContainer[int(item) - 1], globalContent.database.clientContainer[int(client) - 1])
            elif(option == '3'):
                cpf = input('\n digite o cpf do cliente que vai devolver: \n')
                client = self.searchClient(cpf)
                self.giveBack(client)
                self.listClients()
            elif(option == '4'):
                iditem = input('identificador do item: \n')
                item = self.searchItem(iditem)

                name = input('digite o novo nome:\n')
                value = input('digite o novo valor: \n')
                desc = input('digite a nova descrição\n')

                self.updateItem(item, name, -1, value, desc, "")
                self.listItems()
            else:
                break



