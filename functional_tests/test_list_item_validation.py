from .base import FunctionalTest
from unittest import skipIf

class ItemValidationTest(FunctionalTest):
    
    def get_error_element(self):
        return self.browser.find_element_by_css_selector(".has-error")
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit and empty
        # list item. She hits enter with an empty imput box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        # the home page refreshes, and there is an error message saying
        # that the list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # she tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1. Buy milk')
        
        # perversely, she tries to sumbit a second blank item
        self.get_item_input_box().send_keys('\n')
        
        # she receives a similar warning on the list page
        self.check_for_row_in_list_table('1. Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # she can correct it by filling in text
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1. Buy milk')
        self.check_for_row_in_list_table('2. Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edwin goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy stuff\n')
        self.check_for_row_in_list_table('1. Buy stuff')

        # He accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy stuff\n')

        # sees a helpful error message
        self.check_for_row_in_list_table('1. Buy stuff')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # Eunice starts a new list in a way that causes an error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())
        
        # she starts typing and the error clears
        self.get_item_input_box().send_keys('a')
        
        # she is happy to see the error clear
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
        
