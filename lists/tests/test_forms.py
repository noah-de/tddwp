from django.test import TestCase
from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR, 
    ExistingListItemForm, ItemForm
)
from lists.models import Item,List

class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],[EMPTY_LIST_ERROR])

    def test_form_save_handles_saving_to_a_list(self):
        listo = List.objects.create()
        form = ItemForm(data={'text':'regular text'})
        new_item = form.save(for_list=listo)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'regular text')
        self.assertEqual(new_item.list, listo)

class ExistingListItemFormTest(TestCase):

    def test_form_save(self):
        listo = List.objects.create()
        form = ExistingListItemForm(for_list=listo, data={'text': 'hi'})
        new_item = form.save()
        self.assertEqual(new_item, Item.objects.all()[0])

    def test_form_renders_item_text_input(self):
        listo = List.objects.create()
        form = ExistingListItemForm(for_list=listo)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        listo = List.objects.create()
        form = ExistingListItemForm(for_list=listo, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])

    def test_form_validation_for_duplicate_items(self):
        listo = List.objects.create()
        Item.objects.create(list=listo, text='no twins!')
        form = ExistingListItemForm(for_list=listo, data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])