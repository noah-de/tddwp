from django.test import TestCase
from lists.forms import EMPTY_LIST_ERROR, ItemForm

class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],[EMPTY_LIST_ERROR])

    #def test_form_save_handles_saving_to_a_list(self):
    #    form = ItemForm(data={'text':'regular text'})
    #    new_item = form.save()
