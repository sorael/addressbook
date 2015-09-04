# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_contact_from_contacts_page(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    old_contacts = gen.contact.get_contact_list()
    index = randrange(len(old_contacts))
    gen.contact.delete_contact_from_contacts_page(index)
    assert len(old_contacts) - 1 == gen.contact.count()
    new_contacts = gen.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def test_delete_contact_from_edit_page(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    old_contacts = gen.contact.get_contact_list()
    index = randrange(len(old_contacts))
    gen.contact.delete_contact_from_edit_page(index)
    assert len(old_contacts) - 1 == gen.contact.count()
    new_contacts = gen.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
