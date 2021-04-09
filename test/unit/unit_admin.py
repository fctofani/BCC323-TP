import unittest

from src.adminEmployee import AdminEmployee, Employee

import globalContent


class Unit_Admin(unittest.TestCase):
    def test_createCommonEmployee(self):
        common = AdminEmployee.createCommonEmployee(first_name="Lucas", last_name="Natali",
                                                    id=990, self=globalContent.database)

        self.assertEqual(common.first_name, "Lucas")

        self.assertEqual(common.last_name, "Natali")
        self.assertEqual(common.id, 990)

    def test_deleteEmployee(self):
        common = AdminEmployee.createCommonEmployee(first_name="Geraldo", last_name="Pinheiros",
                                                    id=188, self=globalContent.database)
        globalContent.database.employeeContainer.append(common)

        AdminEmployee.deleteEmployee(self, id=188)

        self.assertNotIn(common, globalContent.database.employeeContainer)

    def test_searchEmployee(self):
        emp = AdminEmployee.searchEmployee(self, 990)
        self.assertIn(emp, globalContent.database.employeeContainer)

    def test_updateEmployee(self):
        emp = AdminEmployee.searchEmployee(self, 990)
        AdminEmployee.updateEmployee(self, employee=emp, first_name="Gerolds fitsGerold",
                                     last_name="damaceno", id=123)
        emp = AdminEmployee.searchEmployee(self, 123)

        self.assertEqual(emp.first_name, "Gerolds fitsGerold")
        self.assertEqual(emp.last_name, "damaceno")
        self.assertEqual(emp.id, 123)

    def test_createItem(self):
        item = AdminEmployee.createItem(self, item_name="item 99", id_item=2020,
                                        value=665.43, description="item alguma coisa",
                                        status='available')
        self.assertEqual(item.item_name, "item 99")
        self.assertEqual(item.id_item, 2020)
        self.assertEqual(item.value, 665.43)
        self.assertEqual(item.description, "item alguma coisa")
        self.assertEqual(item.status, 'available')

    def test_deleteItem(self):
        item = AdminEmployee.createItem(self, item_name="item 99", id_item=2020,
                                        value=665.43, description="item alguma coisa",
                                        status='available')
        globalContent.database.itemsContainer.append(item)
        AdminEmployee.deleteItem(self, itemsContainer=globalContent.database.itemsContainer,
                                 id_item=2020)
        self.assertNotIn(item, globalContent.database.itemsContainer)


if __name__ == '__main__':
    unittest.main()
