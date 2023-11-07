#!/usr/bin/python3
"""
customers calss test
"""

from models.customers import Customer
from models.basemodel import BaseModel
import unittest


class test_customer(unittest.TestCase):
    """
    instantiates a test object
    """

    def test_is_subclass(self):
        """Test that Customer is a subclass of BaseModel"""
        customer = Customer()
        self.assertIsInstance(customer, BaseModel)
        self.assertTrue(hasattr(customer, "id"))
        self.assertTrue(hasattr(customer, "created_at"))
        self.assertTrue(hasattr(customer, "updated_at"))

    def test_customer_instance(self):
        """Test that Customer is a subclass of BaseModel"""
        customer = Customer(first='Ahmed', last='Olalekan', sex='male')
        self.assertIsInstance(customer, BaseModel)
        self.assertTrue(hasattr(customer, "id"))
        self.assertTrue(hasattr(customer, "created_at"))
        self.assertTrue(hasattr(customer, "updated_at"))
        self.assertTrue(hasattr(customer, "first"))
        self.assertTrue(hasattr(customer, "last"))
        self.assertTrue(hasattr(customer, "sex"))
        self.assertEqual(customer.first, 'Ahmed')
        self.assertEqual(customer.last, 'Olalekan')
        self.assertEqual(customer.sex, 'male')
