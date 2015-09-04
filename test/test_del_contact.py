# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    old_contacts = gen.contact.get_contact_list()
    gen.contact.delete_first_contact()
    assert len(old_contacts) - 1 == gen.contact.count()
    new_contacts = gen.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_contact_from_edit_page(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    old_contacts = gen.contact.get_contact_list()
    gen.contact.delete_contact_from_edit_page()
    assert len(old_contacts) - 1 == gen.contact.count()
    new_contacts = gen.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
