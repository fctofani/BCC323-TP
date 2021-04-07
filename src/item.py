
class Item:
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description
        self.status = 'Available'

    def print(self):
        print('\nNome: ' + self.name)
        print('Valor (R$): ' + self.value)
        print('Descrição: ' + self.description)
        print('Status: ' + self.status)

