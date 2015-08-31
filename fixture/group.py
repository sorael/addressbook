# -*- coding: utf-8 -*-


class GroupHelper:
    def __init__(self, gen):
        self.gen = gen

    def return_to_groups_page(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.gen.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.gen.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        driver = self.gen.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.gen.driver
        driver.find_element_by_name("selected[]").click()

    def edit_first_group(self, new_group_data):
        driver = self.gen.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.gen.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text("groups").click()

    def count(self):
        driver = self.gen.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))
