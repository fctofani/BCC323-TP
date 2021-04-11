import unittest

from src.adminEmployee import AdminEmployee, Employee

import globalContent


class Unit_Admin(unittest.TestCase):
    def test_createCommonEmployee(self):
        AdminEmployee.createCommonEmployee(first_name="Lucas", last_name="Natali",
                                                    id=990, self=globalContent.database)

        common = AdminEmployee.searchEmployee(self,empid=990)

        self.assertNotEqual(common, None)
        self.assertIn(common, globalContent.database.employeeContainer)
        self.assertEqual(common.first_name, "Lucas")

        self.assertEqual(common.last_name, "Natali")
        self.assertEqual(common.id, 990)

    def test_deleteEmployee(self):
        AdminEmployee.createCommonEmployee(first_name="Geraldo", last_name="Pinheiros",
                                                    id=188, self=globalContent.database)

        common = AdminEmployee.searchEmployee(self, empid=188)
        self.assertNotEqual(common, None)
        self.assertIn(common, globalContent.database.employeeContainer)

        result1 = AdminEmployee.deleteEmployee(self, empid=188)
        result2 = AdminEmployee.deleteEmployee(self, empid=1772)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
        self.assertNotIn(common, globalContent.database.employeeContainer)

    def test_searchEmployee(self):
        emp = AdminEmployee.searchEmployee(self, 990)
        emp2 = AdminEmployee.searchEmployee(self, 8752)

        self.assertEqual(emp2, None)
        self.assertNotEqual(emp, None)
        self.assertIn(emp, globalContent.database.employeeContainer)
        self.assertNotIn(emp2, globalContent.database.employeeContainer)
    def test_updateEmployee(self):
        emp = AdminEmployee.searchEmployee(self, 990)
        AdminEmployee.updateEmployee(self, employee=emp, first_name="Ismael",
                                     last_name="Damaceno", id=123)
        emp = AdminEmployee.searchEmployee(self, 123)

        self.assertEqual(emp.first_name, "Ismael")
        self.assertEqual(emp.last_name, "Damaceno")
        self.assertEqual(emp.id, 123)

    def test_createItem(self):
        AdminEmployee.createItem(self, item_name="item 99", id_item=2020,
                                        value=665.43, description="item alguma coisa",
                                        status='available')
        item = AdminEmployee.searchItem(self, 2020)

        self.assertIn(item, globalContent.database.itemsContainer)
        self.assertEqual(item.item_name, "item 99")
        self.assertEqual(item.id_item, 2020)
        self.assertEqual(item.value, 665.43)
        self.assertEqual(item.description, "item alguma coisa")
        self.assertEqual(item.status, 'available')

    def test_deleteItem(self):
        AdminEmployee.createItem(self, item_name="item 99", id_item=2020,
                                        value=665.43, description="item alguma coisa",
                                        status='available')

        item = AdminEmployee.searchItem(self, 2020)
        item2 = AdminEmployee.searchItem(self, 99999)
        result = AdminEmployee.deleteItem(self, id_item=2020)
        result2 = AdminEmployee.deleteItem(self, id_item=99999)

        self.assertEqual(result, True)
        self.assertEqual(result2, False)
        self.assertNotIn(item2, globalContent.database.itemsContainer)
        self.assertNotIn(item, globalContent.database.itemsContainer)


if __name__ == '__main__':
    unittest.main()
