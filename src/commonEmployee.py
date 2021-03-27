class CommonEmployee(Employee):
    def __init__(self):
        pass
    
    def rent(self, item, client):
        client.listItems.append(item) #status alugado