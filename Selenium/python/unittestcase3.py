import unittest
from selenium import webdriver
@classmethod
def setUpModule():
    print('setup module')
@classmethod
def tearDownModule():
    print('teardown module')
class AppTesting(unittest.TestCase):
    def setUP

    @classmethod
    def setUp(cls):
        print('this is login test')

    @classmethod
    def tearDown(cls):
        print('this is log out test')
    @classmethod
    def setUpClass(self):
        print('open appications')
    @classmethod
    def tearDownClass(self):
        print('close application')

    def test_search(self):
        print('this is search test')

    def test_advancesearch(self):
        print('this is advance search test')

    def test_prepaidRecharge(self):
        print('this is prepaid recharge test')

    def test_postpaidRecharge(self):
        print('this is search test')


if __name__ == "__main__":
    unittest.main()
