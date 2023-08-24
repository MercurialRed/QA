import time

from Python_autotests.pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage


class TestWidgetsPage:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == "What is Lorem Ipsum?" and first_content > 0, "Incorrect title or missing text"
            assert second_title == "Where does it come from?" and second_content > 0, "Incorrect title or missing text"
            assert third_title == "Why do we use it?" and third_content > 0, "Incorrect title or missing text"

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, "The added colors are missing in the input"

        def test_remove_value_from_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, "Value was not delated"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, "The added colors are missing in the input"

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, "The date has not been changed"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, "The date and time have not been changed"

    '''class TestSliderPage:

        def (self, driver):
            _page = SliderPage(driver, "https://demoqa.com/slider")
            _page.open()

    class TestProgressBarPage:

        def (self, driver):
            _page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            _page.open()

    class TestTabsPage:

        def (self, driver):
            _page = TabsPage(driver, "https://demoqa.com/tabs")
            _page.open()

    class TestToolTipsPage:

        def (self, driver):
            _page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            _page.open()

    class TestMenuPage:

        def (self, driver):
            _page = MenuPage(driver, "https://demoqa.com/menu")
            _page.open()

    class TestMenuPage:

        def (self, driver):
            _page = AutoCompletePage(driver, "https://demoqa.com/select-menu")
            _page.open()'''





