from django.contrib.staticfiles.testing import StaticLiveServerCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
import sys

class FunctionalTest(StaticLiveServerCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Herbert came across a to-do app that was on his own desktop. 
        # He finds it at localhost.
        self.browser.get(self.server_url)
    
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
        herbert_list_url = self.browser.current_url
        self.assertRegex(herbert_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1. buy potatoes')
        
        # There is still a text box inviting him to add another item
        # He enters: "wash and peel potatoes" as an item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('wash and peel potatoes')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again, and now shows both items on the list
        self.check_for_row_in_list_table('1. buy potatoes')
        self.check_for_row_in_list_table('2. wash and peel potatoes')
        
        # Francis comes along to the site
        
        ## new browser session to start fresh (no cookies)
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Francis goes to the home page and sees no trace of Herbert's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy potatoes', page_text)
        self.assertNotIn('wash and peel potatoes', page_text)
        
        # Francis enters a new list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, herbert_list_url)
        
        # still no trace of Herbert's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy potatoes', page_text)
        self.assertIn('Buy milk', page_text)
        
        # Herbert wonders if the site will remember his list. Seeing that 
        # the site has generated a unique URL for him -- there is some 
        # text to that effect.
class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        
        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2, 512, delta=5
        )
        
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2, 512, delta=5
        )
    
class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit and empty
        # list item. She hits enter with an empty imput box
        
        # the home page refreshes, and there is an error message saying
        # that the list items cannot be blank
        
        # she tries again with some text for the item, which now works
        
        # perversely, she tries to sumbit a second blank item
        
        # she receives a similar warning on the list page
        
        # she can correct it by filling in text
        self.fail('write this test!')
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')
