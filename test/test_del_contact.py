# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    gen.contact.delete_first_contact()

def test_delete_contact_from_edit_page(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    gen.contact.delete_contact_from_edit_page()
