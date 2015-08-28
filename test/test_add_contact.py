# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(gen):
    gen.contact.create(Contact(
        firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
        photo="E:\selenium\\addressbook\\files\contact_photo.jpg", title="title", company="company", address="address",
        home="home", mobile="mobile", work="work", fax="fax", email2="email2@email2.ru", email3="email3@email3.ru",
        homepage="homepage.com", bday="2", bmonth="February", byear="1993", aday="8", amonth="June", ayear="2000",
        address2="address2", phone2="phone2", notes="notes"))
