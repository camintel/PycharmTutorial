import unittest
from main_source import  hellow_world

class MyTestCase(unittest.TestCase):
    def test_hello_message(self):
        self.assertEqual("Hello, CIS 189!", hellow_world.hello_message())  # add assertion here

if __name__ == '__main__':
    unittest.main()
