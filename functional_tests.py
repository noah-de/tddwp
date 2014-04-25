#!/usr/local/bin/python3

from selenium import webdriver
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
        self.fail('Finish the test') 
        # He is allowed to enter a to-do item right away
        
        # He types " buy potatoes" into a text box
        
        # When he hits enter, the page updates and now the page lists
        # "1: buy potatoes" as an item in a to-do list
        
        # There is still a text box inviting him to add another item
        # He enters: "wash and peel potatoes" as an item.
        
        # The page updates again, and now shows both items on the list
        
        # Herbert wonders if the site will remember his list. Seeing that 
        # the site has generated a unique URL for him -- there is some 
        # text to that effect.
        
        # Visiting that URL - his to-do list is still there
if __name__ == '__main__':
    unittest.main(warnings='ignore')
