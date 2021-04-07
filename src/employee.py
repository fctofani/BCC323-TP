class Employee:

    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        
    def rentItem(self, system):
        print('\n\n------- ESCOLHA O ITEM A SER ALUGADO ------')
        idx = 1
        for item in system.itemsContainer:
            print('(' + str(idx) + ') - ' + item.name)
            idx = idx + 1
        chosenItemIdx = input()
        chosenItem = system.itemsContainer[int(chosenItemIdx) - 1]

        if(chosenItem.status == 'Rented'):
            print('Ops... Este item já está alugado!')
        else:    
            print('\n\n------- ESCOLHA O CLIENTE QUE DESEJA ALUGAR ------')
            idx = 1
            for client in system.clientContainer:
                print('(' + str(idx) + ') - ' + client.first_name + ' ' + client.last_name)
                idx = idx + 1
            chosenClientIdx = input()

            chosenClient = system.clientContainer[int(chosenClientIdx) - 1]
            chosenItem.status = 'Rented'
            chosenClient.rentedItems.append(chosenItem)
            print('Item alugado com sucesso!')

