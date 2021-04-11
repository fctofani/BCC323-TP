
import unittest
from src.adminEmployee import Employee, AdminEmployee
from src.commonEmployee import CommonEmployee
import globalContent


class Funcional_CommonEmployee(unittest.TestCase):
    def test_funcional_commonEmp(self):
        CommonEmployee.createClient(self, first_name="Fulano",
                                              last_name="test", cpf="133.444.566-72",
                                              email="email@email.com", phone="1279317")

        CommonEmployee.createClient(self, first_name="Ciclano",
                                              last_name="vintedois", cpf="444.222.566-72",
                                              email="ciclano@email.com", phone="9999261")

        client1= CommonEmployee.searchClient(self, "133.444.566-72")
        client2= CommonEmployee.searchClient(self, "444.222.566-72")

        self.assertNotEqual(client1, None)
        self.assertNotEqual(client2, None)

        CommonEmployee.updateClient(self, client1, first_name="Beltrano",
                                    last_name="Aroldo", email="email@jesus.com")

        CommonEmployee.updateClient(self, client2, first_name="Carlos",
                                    last_name="Alberto", cpf="997.143.777-91",
                                    email="carlos@email.com")

        client1 = CommonEmployee.searchClient(self, "133.444.566-72")
        client2 = CommonEmployee.searchClient(self, "997.143.777-91")
        self.assertNotEqual(client1, None)
        self.assertNotEqual(client2, None)

        self.assertEqual(client1.first_name, "Beltrano")
        self.assertEqual(client1.last_name, "Aroldo")
        self.assertEqual(client1.email, "email@jesus.com")

        self.assertEqual(client2.first_name, "Carlos")
        self.assertEqual(client2.last_name, "Alberto")
        self.assertEqual(client2.email, "carlos@email.com")
        self.assertEqual(client2.cpf, "997.143.777-91")

        item1 = CommonEmployee.searchItem(self, 1)

        item2 = CommonEmployee.searchItem(self, 2)
        item3 = CommonEmployee.searchItem(self, 3)

        self.assertNotEqual(item1, None)
        self.assertNotEqual(item2, None)
        self.assertNotEqual(item3, None)




        r1 = CommonEmployee.rent(self, item1, client1)
        r2 = CommonEmployee.rent(self, item1, client1)
        r3 = CommonEmployee.rent(self, item2, client2)
        r4 = CommonEmployee.rent(self, item2, client2)


        self.assertEqual(r1, True)
        self.assertEqual(r2, False)
        self.assertEqual(r3, True)
        self.assertEqual(r4, False)

        CommonEmployee.deleteClient(self, "997.143.777-91")

        cli = CommonEmployee.searchClient(self, "997.143.777-91")
        self.assertEqual(cli, None)
        self.assertNotIn(cli, globalContent.database.clientContainer)


class Funcional_AdminEmployee(unittest.TestCase):
    def test_funcional_adminEmp(self):
        AdminEmployee.createClient(self, first_name="Fulano",
                                            last_name="test", cpf="133.444.566-72",
                                            email="email@email.com", phone="1279317")


        AdminEmployee.createItem(self, item_name="item Y",
                                         id_item=55, value=44.5, description="Item qualquer",
                                         status="available")
        AdminEmployee.createItem(self, item_name="item Z",
                                         id_item=98, value=88.5, description="Item XO",
                                         status="available")

        client = AdminEmployee.searchClient(self,"133.444.566-72")
        item1 = AdminEmployee.searchItem(self, 55)
        item2 = AdminEmployee.searchItem(self, 98)

        self.assertNotEqual(client, None)
        self.assertNotEqual(item1, None)
        self.assertNotEqual(item2, None)

        r1 = AdminEmployee.rent(self, item1, client)
        r2 = AdminEmployee.rent(self, item2, client)

        self.assertEqual(r1, True)
        self.assertEqual(r2, True)

        AdminEmployee.deleteItem(self, 98)

        it = AdminEmployee.searchItem(self, 98)

        self.assertNotEqual(it, None) #Itens alugados não podem ser removidos
        self.assertIn(it, globalContent.database.itemsContainer)





if __name__ == '__main__':
    unittest.main()
