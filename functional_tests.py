#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Herbert came across a to-do app that was on his own desktop. 
        # He finds it at localhost.
        self.browser.get('http://localhost:8000')
        
        # He sees that the page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)

        # He is allowed to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),'Enter a to-do item'
        )
        
        # He types " buy potatoes" into a text box
        inputbox.send_keys('buy potatoes')
        
        # When he hits enter, the page updates and now the page lists
        # "1: buy potatoes" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        import time
        #time.sleep(3)
        self.assertTrue(
           any(row.text == '1. buy potatoes' for row in rows),
           "New to-do item did not appear in table -- its text was: \n%s" % (
               table.text,)
        )
        
        # There is still a text box inviting him to add another item
        # He enters: "wash and peel potatoes" as an item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('wash and peel potatoes')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again, and now shows both items on the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. buy potatoes', [row.text for row in rows])
        self.assertIn('wash and peel potatoes', [row.text for row in rows])

        self.fail('Finish the test')

        # Herbert wonders if the site will remember his list. Seeing that 
        # the site has generated a unique URL for him -- there is some 
        # text to that effect.
        
        # Visiting that URL - his to-do list is still there
if __name__ == '__main__':
    unittest.main(warnings='ignore')
