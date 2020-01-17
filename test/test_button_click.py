import unittest
from selenium import webdriver
from pathlib import Path
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

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

if __name__ == "__main__":
    unittest.main()
