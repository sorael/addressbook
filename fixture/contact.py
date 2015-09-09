# -*- coding: utf-8 -*-
from model.contact import Contact
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import re


class ContactHelper:
    def __init__(self, gen):
        self.gen = gen

    def create(self, contact):
        self.click_add_new_button()
        self.fill_contact_form(contact)
        self.click_submit_button()
        self.return_to_home_page()
        self.contact_cache = None

    def click_add_new_button(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("add new").click()

    def click_submit_button(self):
        driver = self.gen.driver
        driver.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        driver = self.gen.driver
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if contact.bday is not None:
            Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth is not None:
            Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        if contact.aday is not None:
            Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        if contact.amonth is not None:
            Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        driver = self.gen.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_contact_from_contacts_page(self, index):
        driver = self.gen.driver
        self.open_home_page()
        self.select_contact_by_index(index)
        self.delete_button_click()
        driver.switch_to_alert()
        Alert(driver).accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        driver = self.gen.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def open_home_page(self):
        driver = self.gen.driver
        if not (len(driver.find_elements_by_xpath("//input[@value='Send e-Mail']")) == 1):
            driver.find_element_by_link_text("home").click()

    def delete_contact_from_edit_page(self, index):
        self.open_home_page()
        self.edit_button_click(index)
        self.delete_button_click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_button_click(self):
        driver = self.gen.driver
        driver.find_element_by_xpath("//input[@value='Delete']").click()

    def return_to_home_page(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("home").click()

    def add_next(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("add next").click()

    def edit_contact_from_home_page(self, index, new_contact_data):
        driver = self.gen.driver
        self.open_home_page()
        self.edit_button_click(index)
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_from_contact_page(self, index, new_contact_data):
        driver = self.gen.driver
        self.open_home_page()
        self.detail_button_click(index)
        driver.find_element_by_name("modifiy").click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_button_click(self, index):
        driver = self.gen.driver
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def detail_button_click(self, index):
        driver = self.gen.driver
        driver.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def count(self):
        driver = self.gen.driver
        self.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    def create_after_added_contact(self, contact):
        self.click_add_new_button()
        self.fill_contact_form(contact)
        self.click_submit_button()
        self.add_next()
        self.create(contact)
        self.contact_cache = None

    def open_contact_to_edit(self, index):
        # driver = self.gen.driver
        self.open_home_page()
        self.edit_button_click(index)

    def open_contact_to_view(self, index):
        # driver = self.gen.driver
        self.open_home_page()
        self.detail_button_click(index)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.gen.driver
            self.contact_cache = []
            for i in driver.find_elements_by_xpath("//tr[@name='entry']"):
                cells = i.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                contact_id = i.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=contact_id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        driver = self.gen.driver
        self.open_contact_to_edit(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        contact_id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=contact_id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_info_from_view_page(self, index):
        driver = self.gen.driver
        self.open_contact_to_view(index)
        names =  driver.find_element_by_xpath("//div[@id='content']/b").text.split(" ")
        firstname = names[0]
        lastname = names[2]
        text = driver.find_element_by_id("content").text
        try:
            homephone = re.search("H: (.*)", text).group(1)
        except:
            homephone = None
        try:
            mobilephone = re.search("M: (.*)", text).group(1)
        except:
            mobilephone = None
        try:
            workphone = re.search("W: (.*)", text).group(1)
        except:
            workphone = None
        try:
            secondaryphone = re.search("P: (.*)", text).group(1)
        except:
            secondaryphone = None
        return Contact(firstname=firstname, lastname=lastname, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)
