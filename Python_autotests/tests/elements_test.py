import random
import time

from Python_autotests.pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, \
    LinksPage, UploadAndDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            test_box_page = TextBoxPage(driver, "https://demoqa.com/text-box/")
            test_box_page.open()
            full_name, email, current_address, permanent_address = test_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = test_box_page.check_filled_form()

            assert full_name == output_name, "the full_name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current_address does not match"
            assert permanent_address == output_per_addr, "the permanent_address does not match"
            time.sleep(2)

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox/")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkboxes have not been selected"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button/")
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', '"Yes" have not been selected'
            assert output_impressive == 'Impressive', '"Impressive" have not been selected'
            assert output_no == 'No', '"No" have not been selected'

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables/")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print((table_result))
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables/")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables/")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables/")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            web_table_page.check_deleted()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables/")
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "The number of rows in the table has not been changed or has changed incorectly"

    class TestButtonPage:
        def test_different_click_on_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons/")
            button_page.open()
            time.sleep(1)
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            time.sleep(3)
            print(click)
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The click button was not pressed"

    class TestLinksPage:
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links/")
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links/")
            links_page.open()
            response_code = links_page.check_broken_link("https://demoqa.com/bad-request/")
            assert response_code == 400, "The link works or the status code is 400"

        def test_invalid_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links/")
            links_page.open()
            response_code = links_page.check_invalid_link("https://demoqa.com/invalid-url/")
            assert response_code == 404, "The link works or the status code is 404"

    class TestUploadAndDownload:
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download/")
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "The file has not been downloaded"

        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download/")
            upload_download_page.open()
            upload_download_page.upload_file()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "The file has not been uploaded"

    class TestDynamicProperties:
        def test_dynamic_text_id(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties/")
            dynamic_properties_page.open()
            text_id1 = dynamic_properties_page.check_text_id_change()
            driver.refresh()
            text_id2 = dynamic_properties_page.check_text_id_change()
            assert text_id1 != text_id2, "Text ID has not been changed"

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties/")
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, "Button did not enable after 5 seconds"

        def test_dynamic_color_change(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties/")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_change_of_color()
            assert color_after != color_before, "Colors have not been changed"

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties/")
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, "Button did not appear after 5 seconds"


