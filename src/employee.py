from client import Client
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
    

    def createClient(self, first_name, last_name, cpf, email, password):
        client = Client(first_name, last_name, cpf, email, password)
        return client
        
    def searchClient(self, clientContainer, cpf):
        for i in clientContainer:
            if i.cpf == cpf :
                return i
        
    def deleteClient(self, clientContainer, cpf):
        for i in clientContainer:
            if i.cpf == cpf:
                clientContainer.remove(i)
                
        
    def updateClient(self, clientContainer, client, 
        first_name = "", last_name = "",
         cpf = "", email = "", phone = ""):
        for i in clientContainer:
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
              
    def listClients(self, clients):
        print("----------Lista de clientes-------")
        for i in clients:
            print(i)
        

    def rent(self, item, client):
        if item.status == 'rented':
            print('item já está alugado.')
            return false
        else:
            item.status = 'rented'
            print("item alugado com sucesso")
            client.listItems.append(item) #status alugado
            return true

    def updateItem(self, itemsContainer, item, item_name="", id_item=-1,
        value=-1, description="", status = ""
    ):
        for i in itemsContainer:
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

        
    def searchItem(self, itemsContainer, id_item):
        for i in itemsContainer:
            if i.id_item == id_item:
                return i
        
    def listItems(self, itemsContainer):
        for i in itemsContainer:
            print(i)
        