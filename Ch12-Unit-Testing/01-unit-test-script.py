import unittest
import testObject

if __name__ == '__main__':
    unittest.main()

class TestCapitalize(unittest.TestCase):
    def test_capitalize_correct(self):
        capitalized_result = testObject.capitalize('hello')
        self.assertEqual(capitalized_result, 'Hello')

    def test_capitalize_incorrect(self):
        capitalized_result = testObject.capitalize('python is good')
        self.assertEqual(capitalized_result, 'Python is good')