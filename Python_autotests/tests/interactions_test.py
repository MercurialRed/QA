from Python_autotests.pages.interactions_page import SortablePage


class TestInteractionsPage:

    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"


'''
    class TestSelectablePage:

        def test_(self, driver):
            selectable_page = (driver, "https://demoqa.com/selectable")
            selectable_page.open()


    class TestResizablePage:

        def test_(self, driver):
            resizable_page = (driver, "https://demoqa.com/resizable")
            resizable_page.open()


    class TestDroppablePage:

        def test_(self, driver):
            droppable_page = (driver, "https://demoqa.com/droppable")
            droppable_page.open()


    class TestDraggablePage:

        def test_(self, driver):
            draggable_page = (driver, "https://demoqa.com/dragabble")
            draggable_page.open()'''


