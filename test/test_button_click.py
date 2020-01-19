import unittest
from selenium import webdriver
from pathlib import Path

class ButtonClickTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_verify_header_text(self):
        driver = self.driver
        html_file = Path.cwd() / "main.html"
        driver.get(html_file.as_uri())
        button1 = driver.find_element_by_id("button1")
        button1.click()
        message_div = driver.find_element_by_id("message")
        self.assertEqual(message_div.text, "The button was clicked.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
