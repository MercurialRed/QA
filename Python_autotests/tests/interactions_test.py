from Python_autotests.pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractionsPage:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "No elements were selected"
            assert len(item_grid) > 0, "No elements were selected"

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, "Maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "Minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "Resizable has not been changed"



'''
    class TestDroppablePage:

        def test_(self, driver):
            droppable_page = (driver, "https://demoqa.com/droppable")
            droppable_page.open()


    class TestDraggablePage:

        def test_(self, driver):
            draggable_page = (driver, "https://demoqa.com/dragabble")
            draggable_page.open()'''
