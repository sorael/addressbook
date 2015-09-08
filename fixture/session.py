# -*- coding: utf-8 -*-


class SessionHelper:
    def __init__(self, gen):
        self.gen = gen

    def logout(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.gen.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        # driver = self.gen.driver
        return self.get_logged_user() == username

    def get_logged_user(self):
        driver = self.gen.driver
        return driver.find_element_by_xpath("//form[@name='logout']/b").text[1:-1]

    def login(self, username, password):
        driver = self.gen.driver
        self.gen.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type='submit']").click()

    def ensure_login(self, username, password):
        # driver = self.gen.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
