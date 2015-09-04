# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    old_contacts = gen.contact.get_contact_list()
    contact = Contact(firstname="New firstname")
    contact.id = old_contacts[0].id
    gen.contact.edit_first_contact(contact)
    assert len(old_contacts) == gen.contact.count()
    new_contacts = gen.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_contact_middlename(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(middlename="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(middlename="New middlename"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_lastname(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(lastname="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(lastname="New lastname"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_nickname(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(nickname="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(nickname="New nickname"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_photo(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(photo=""))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(photo="New photo"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_title(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(title="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(title="New title"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_company(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(company="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(company="New company"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_address(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(address="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(address="New address"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_home(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(home="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(home="New home"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_mobile(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(mobile="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(mobile="New mobile"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_work(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(work="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(work="New work"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_fax(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(fax="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(fax="New fax"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_email2(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(email2="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(email2="New email2"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_email3(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(email3="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(email3="New email3"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_homepage(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(homepage="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(homepage="New homepage"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_bday(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(bday="6"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(bday="6"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_bmonth(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(bmonth="July"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(bmonth="July"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_byear(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(byear="1111"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(byear="1111"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_aday(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(aday="6"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(aday="6"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_amonth(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(amonth="July"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(amonth="July"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_ayear(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(ayear="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(ayear="1111"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_address2(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(address2="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(address2="New address2"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_phone2(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(phone2="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(phone2="New phone2"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_notes(gen):
#     if gen.contact.count() == 0:
#         gen.contact.create(Contact(notes="test"))
#     old_contacts = gen.contact.get_contact_list()
#     gen.contact.edit_first_contact(Contact(notes="New notes"))
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
