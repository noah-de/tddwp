from unittest import skip
from .base import FunctionalTest
    
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
