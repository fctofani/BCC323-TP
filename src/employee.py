class Employee:

    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        

    def createClient(self, first_name, last_name, cpf, email, password):
        pass
    def deleteClient(self, cpf):
        pass
    def updateClient(self, first_name, last_name, cpf, email, password):
        pass
    def listClients(self):
        pass

    def rent(self, item, client):
        if item.status == 'rented':
            print('item já está alugado.')
            return False
        else:
            item.status = 'rented'
            print("item alugado com sucesso")
            client.rentedItems.append(item) #status alugado
            return True

