import unittest
from uuid import uuid4
from main import Shopping


def generate_email(size):
    return [f'test0{i}' for i in range(1, size+1)]


class TestShoppingClass(unittest.TestCase):

    def test_raise_exception_shopping_list_empty(self):
        shopping_list = []
        email_list = ['test']

        with self.assertRaises(ValueError) as cm:
            Shopping(shopping_list, email_list)
        exception = cm.exception

        self.assertEqual(
            str(exception),
            'Shopping list or email list can not be empty.'
        )

    def test_raise_exception_email_list_empty(self):
        shopping_list = [{'name': 'apple', 'amount': 10, 'value': 10}]
        email_list = []

        with self.assertRaises(ValueError) as cm:
            Shopping(shopping_list, email_list)
        exception = cm.exception

        self.assertEqual(
            str(exception),
            'Shopping list or email list can not be empty.'
        )
    
    def test_raise_exception_invalid_item_structure(self):
        shopping_list = [{'name': 10, 'amount': 10, 'value': 10}]
        email_list = ['test']

        with self.assertRaises(Exception) as cm:
            Shopping(shopping_list, email_list)
        exception = cm.exception

        self.assertEqual(
            str(exception),
            'Invalid item structure.'
        )

    def test_one_item_one_email_ok(self):
        shopping_list = [{'name': 'item01', 'amount': 10, 'value': 10}]
        email_list = ['test']
        email_map = Shopping(shopping_list, email_list).divide_equally()

        self.assertEqual(email_map['test'], 100)

    def test_two_items_one_email_ok(self):
        shopping_list = [
            {'name': 'item01', 'amount': 10, 'value': 10},
            {'name': 'item02', 'amount': 5, 'value': 2},
        ]
        email_list = ['test']
        email_map = Shopping(shopping_list, email_list).divide_equally()

        self.assertEqual(email_map['test'], 110)

    def test_two_items_one_email_ok(self):
        shopping_list = [
            {'name': 'item01', 'amount': 10, 'value': 10},
            {'name': 'item02', 'amount': 5, 'value': 2},
        ]
        email_list = ['test']
        email_map = Shopping(shopping_list, email_list).divide_equally()

        self.assertEqual(email_map['test'], 110)

    def test_two_items_two_emails_ok(self):
        shopping_list = [
            {'name': 'item01', 'amount': 10, 'value': 10},
            {'name': 'item02', 'amount': 5, 'value': 2},
        ]
        email_list = ['test1', 'test2']
        email_map = Shopping(shopping_list, email_list).divide_equally()

        self.assertEqual(email_map['test1'], 55)
        self.assertEqual(email_map['test2'], 55)

    def test_three_items_five_emails_ok(self):
        shopping_list = [
            {'name': 'item01', 'amount': 300, 'value': 50},
            {'name': 'item02', 'amount': 5454, 'value': 478},
            {'name': 'item03', 'amount': 333, 'value': 2}
        ]
        email_list = generate_email(5)
        email_map = Shopping(shopping_list, email_list).divide_equally()
        expected_values = [524536, 524536, 524536, 524535, 524535]

        for i, email in enumerate(email_list):
            self.assertEqual(email_map[email], expected_values[i])

    def test_three_items_ten_emails_ok(self):
        shopping_list = [
            {'name': 'item01', 'amount': 1, 'value': 15},
            {'name': 'item02', 'amount': 1, 'value': 15},
            {'name': 'item03', 'amount': 1, 'value': 15}
        ]
        email_list = generate_email(10)
        email_map = Shopping(shopping_list, email_list).divide_equally()
        expected_values = [5, 5, 5, 5, 5, 4, 4, 4, 4, 4]

        for i, email in enumerate(email_list):
            self.assertEqual(email_map[email], expected_values[i])

    def test_three_items_twelve_emails_ok(self):
        shopping_list = [
            {'name': 'item01', 'amount': 1, 'value': 15},
            {'name': 'item02', 'amount': 1, 'value': 15},
            {'name': 'item03', 'amount': 1, 'value': 15}
        ]
        email_list = generate_email(12)
        email_map = Shopping(shopping_list, email_list).divide_equally()
        expected_values = [4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3]

        for i, email in enumerate(email_list):
            self.assertEqual(email_map[email], expected_values[i])

    def test_one_item_thirteen_emails_ok(self):
        shopping_list = [
            {'name': 'item01', 'amount': 1, 'value': 56456},
        ]
        email_list = generate_email(13)
        email_map = Shopping(shopping_list, email_list).divide_equally()
        expected_values = [4343, 4343, 4343, 4343, 4343, 4343, 4343, 4343, 4343, 4343, 4342, 4342, 4342]

        for i, email in enumerate(email_list):
            self.assertEqual(email_map[email], expected_values[i])