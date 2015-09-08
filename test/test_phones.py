# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import re


def test_phones_on_home_page(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    index = randrange(gen.contact.count())
    contact_from_home_page = gen.contact.get_contact_list()[index]
    contact_from_edit_page = gen.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_like_on_home_page(contact_from_edit_page)

#TODO: прочитать список телефонов со страницы контакта
def test_phones_on_contact_view_page(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    index = randrange(gen.contact.count())
    contact_from_edit_page = gen.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = gen.contact.get_contact_info_from_view_page(index)
    assert contact_from_view_page.all_phones_from_view_page == merge_phones_like_like_on_view_page(contact_from_edit_page)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None,
                          [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
