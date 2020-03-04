#This program tests the functionality of the employees.py program
#There will be two tests, the first for the default raise
#The second will be for a custom raise

import unittest
from employees import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        """
           Create an employee profile and custom raise amounts
        """
        first_name = 'Tom'
        last_name = 'Kelly'
        salary = 20000
        self.profile = Employee(first_name, last_name, salary)
        self.default = 25000
        self.bump = 27000

    def test_give_default_raise(self):
        """Test the default raise amount"""
        self.assertEqual(self.default, self.profile.give_raise())

    def test_give_custom_raise(self):
        """Test the custom raise amount"""
        self.assertEqual(self.bump, self.profile.give_raise(7000))

if __name__ == '__main__':
    unittest.main() 
