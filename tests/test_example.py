
import unittest
from selenium import webdriver

class TestExample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://example.com')

    def test_title(self):
        self.assertEqual(self.driver.title, 'Example Domain')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
