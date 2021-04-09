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
        return client
        
    def searchClient(self, cpf):
        for i in globalContent.database.clientContainer:
            if i.cpf == cpf :
                return i
        
    def deleteClient(self, cpf):
        for i in globalContent.database.clientContainer:
            if i.cpf == cpf:
                globalContent.database.clientContainer.remove(i)
                
        
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
            option = input('\n----- MENU ITENS ----- \n'
                            + '(1) - Listar Clientes\n'
                            + '(2) - Adicionar Cliente\n'
                            + '(3) - Editar Cliente\n'
                            + '(4) - Remover Cliente\n'
                            + '(5) - SAIR\n')
            
            if(option == '1'): self.listClients()
            elif(option == '2'): print('Ainda não desenvolvido totalmente.')
            elif(option == '3'): print('Ainda não desenvolvido totalmente.')
            elif(option == '4'): print('Ainda não desenvolvido totalmente.')
            elif(option == '5'): break

    def showMenuItems(self):
        while(True):
            option = input('\n----- MENU ITENS ----- \n'
                            + '(1) - Listar Itens\n'
                            + '(2) - Alugar Item\n'
                            + '(3) - SAIR\n')

            if(option == '1'): self.listItems()
            elif(option == '2'):
                self.listItems()
                item = input('\nItem que será alugado: ')
                self.listClients()
                client = input('\nCliente a alugar: ')
                self.rent(globalContent.database.itemsContainer[int(item) - 1], globalContent.database.clientContainer[int(client) - 1])
            elif(option == '3'): break


