import time
import random

from selenium.webdriver.common.by import By

from Python_autotests.generator.generator import generated_person
from Python_autotests.pages.base_page import BasePage
from Python_autotests.locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, \
    RadioButtonPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        button_submit = self.element_is_clickable(self.locators.SUBMIT)
        self.go_to_element(button_submit)
        button_submit.click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        print(data)
        return str(data).replace(' ', '').replace('.', '').replace('doc', '').lower()

    def get_output_result(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        print(data)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                    'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text