# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(gen):
    old_contacts = gen.contact.get_contact_list()
    contact = Contact(
        firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
        photo="E:\selenium\\addressbook\\files\contact_photo.jpg", title="title", company="company", address="address",
        home="home", mobile="mobile", work="work", fax="fax", email2="email2@email2.ru", email3="email3@email3.ru",
        homepage="homepage.com", bday="2", bmonth="February", byear="1993", aday="8", amonth="June", ayear="2000",
        address2="address2", phone2="phone2", notes="notes")
    gen.contact.create(contact)
    assert len(old_contacts) + 1 == gen.contact.count()
    new_contacts = gen.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_contact_after_added_contact(gen):
#     old_contacts = gen.contact.get_contact_list()
#     contact = Contact(
#         firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
#         photo="E:\selenium\\addressbook\\files\contact_photo.jpg", title="title", company="company", address="address",
#         home="home", mobile="mobile", work="work", fax="fax", email2="email2@email2.ru", email3="email3@email3.ru",
#         homepage="homepage.com", bday="2", bmonth="February", byear="1993", aday="8", amonth="June", ayear="2000",
#         address2="address2", phone2="phone2", notes="notes")
#     gen.contact.create_after_added_contact(contact)
#     new_contacts = gen.contact.get_contact_list()
#     assert len(old_contacts) + 2 == gen.contact.count()
#     new_contacts = gen.contact.get_contact_list()
#     old_contacts.append(contact)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)