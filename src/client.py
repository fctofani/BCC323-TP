class Client:
    def __init__(self, first_name, last_name, cpf, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.email = email

        self.phone = phone
        self.rentedItems = []
        

    def __str__(self):
        return "First Name: {}, Last Name: {}, CPF: {}, Email: {}, Phone: {}, Rented Items {}".format(
            self.first_name, self.last_name, self.cpf, self.email, self.phone, self.rentedItems
        )


