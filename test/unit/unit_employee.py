import unittest
import globalContent
from src.employee import Employee


class Unit_Employee(unittest.TestCase):
    def test_createClient(self):
        Employee.createClient(self, first_name="Julia", last_name="Pereira",
                              email="julia@email.com", cpf="133.666.662-99",
                              phone="986326282")

        client = Employee.searchClient(self, "133.666.662-99")
        self.assertNotEqual(client, None)
        self.assertIn(client, globalContent.database.clientContainer)
        self.assertEqual(client.first_name, "Julia")
        self.assertEqual(client.last_name, "Pereira")
        self.assertEqual(client.email, "julia@email.com")
        self.assertEqual(client.phone, "986326282")

    def test_updateClient(self):
        Employee.createClient(self, first_name="Julia", last_name="Pereira",
                              email="julia@email.com", cpf="133.666.662-99",
                              phone="986326282")

        client = Employee.searchClient(self, "133.666.662-99")

        Employee.updateClient(self, client=client, first_name="Janaina", last_name="Pereira",
                              email="janaina@email.com",
                              cpf="444.444.222-88",
                              phone="882211334")

        client = Employee.searchClient(self, "444.444.222-88")
        self.assertEqual(client.first_name, "Janaina")
        self.assertEqual(client.last_name, "Pereira")
        self.assertEqual(client.email, "janaina@email.com")
        self.assertEqual(client.cpf, "444.444.222-88")
        self.assertEqual(client.phone, "882211334")

    def test_deleteClient(self):
        Employee.createClient(self, first_name="Julia", last_name="Pereira",
                              email="julia@email.com", cpf="133.666.662-99",
                              phone="986326282")

        client = Employee.searchClient(self, "133.666.662-99")
        client2 = Employee.searchClient(self, "000.000.000-00")

        result1 = Employee.deleteClient(self, cpf="133.666.662-99")
        result2 = Employee.deleteClient(self, cpf="000.000.000-00")

        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
        self.assertNotIn(client, globalContent.database.clientContainer)
        self.assertNotIn(client2, globalContent.database.clientContainer)

    def test_searchClient(self):
        client = Employee.searchClient(self, "888.225.763-72")
        client2 = Employee.searchClient(self, "212")

        self.assertNotEqual(client, None)
        self.assertIn(client, globalContent.database.clientContainer)
        self.assertEqual(client2, None)
        self.assertNotIn(client2, globalContent.database.clientContainer)

    def test_searchItem(self):
        item = Employee.searchItem(self, 1)
        item2 = Employee.searchItem(self, 999)

        self.assertNotEqual(item, None)
        self.assertIn(item, globalContent.database.itemsContainer)
        self.assertEqual(item2, None)
        self.assertNotIn(item2, globalContent.database.itemsContainer)

    def test_updateItem(self):
        item = Employee.searchItem(self, 1)
        Employee.updateItem(self, item=item, item_name="item X", id_item=955,
                            value=998, description="item X é bom", status="rented")

        item = Employee.searchItem(self, 955)
        self.assertEqual(item.item_name, "item X")
        self.assertEqual(item.id_item, 955)
        self.assertEqual(item.value, 998)
        self.assertEqual(item.description, "item X é bom")
        self.assertEqual(item.status, "rented")

    def test_rent(self):
        item = Employee.searchItem(self, 1)
        client = Employee.searchClient(self, '118.008.212-66')
        r1 = Employee.rent(self, item, client)
        r2 = Employee.rent(self, item, client)
        self.assertEqual(r1, True)
        self.assertEqual(r2, False)


if __name__ == '__main__':
    unittest.main()
