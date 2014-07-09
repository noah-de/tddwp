#!/usr/local/bin/python3
from django.test import TestCase

from lists.models import Item, List
from lists.views import home_page
from django.core.exceptions import ValidationError

class ListAndItemModelsTest(TestCase):

    def test_saving_and_retreiving_items(self):
        listo = List()
        listo.save()
        
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = listo
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = listo
        second_item.save()
        
        saved_list = List.objects.first()
        self.assertEqual(saved_list, listo)
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, listo)
        
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, listo)

    def test_cannot_save_empty_list_items(self):
        listo = List.objects.create()
        item = Item(list=listo, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_get_absolute_url(self):
        listo = List.objects.create()
        self.assertEqual(listo.get_absolute_url(), '/lists/%d/' % (listo.id,))