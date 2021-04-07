from employee import Employee
from item import Item
from client import Client


class AdminEmployee(Employee):
    def __init__(self, first_name, last_name):
        super(AdminEmployee, self).__init__(first_name, last_name, 'Admin')
        pass

    def createItem(self, system):
        print('\n\n------ CRIAR ITEM ------\n\n')
        name = input('Nome:')
        value = input('Valor (R$):')
        description = input('Descrição:')

        system.itemsContainer.append(Item(name, value, description))
        print('\nItem adicionado com sucesso!\n')



    
