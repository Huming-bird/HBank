#!/usr/bin/python3
"""
customers calss test
"""

from models.customers import Customer
from tests.test_models.test_basemodel import test_basemodel


class test_customer(test_basemodel):
    """
    instantiates a test object
    """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Customer"
        self.value = Customer

    def test_first(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first), str)

    def test_last(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)
