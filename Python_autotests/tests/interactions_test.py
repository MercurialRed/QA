import time

from Python_autotests.pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, \
    DraggablePage


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

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "The element has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text_acceptable = droppable_page.drop_acceptable()
            driver.refresh()
            text_not_acceptable = droppable_page.drop_not_acceptable()
            assert text_acceptable == "Dropped!", "The dropped element has not been accepted"
            assert text_not_acceptable == "Drop here", "The dropped element has been accepted"

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text_not_greedy_outer, text_not_greedy_inner = droppable_page.drop_prevent_propogation_not_greedy()
            text_greedy_outer, text_greedy_inner = droppable_page.drop_prevent_propogation_greedy()
            assert text_not_greedy_outer == "Dropped!", "The elements' texts have not been changed"
            assert text_not_greedy_inner == "Dropped!", "The elements' texts have not been changed"
            assert text_greedy_outer == "Outer droppable", "The elements' texts have been changed"
            assert text_greedy_inner == "Dropped!", "The elements' texts have not been changed"

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_revert_before, will_revert_after = droppable_page.drop_revert_draggable('will_revert')
            driver.refresh()
            not_revert_before, not_revert_after = droppable_page.drop_revert_draggable('not_revert')
            assert will_revert_before != will_revert_after, "The element has not been reverted"
            assert not_revert_before == not_revert_after, "The element has been reverted"

    class TestDraggablePage:

        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "The position of the box has not been changed"

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, "Box position has not changed or there has been a shift in the y-axis"
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, "Box position has not changed or there has been a shift in the y-axis"
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, "Box position has not changed or there has been a shift in the x-axis"
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, "Box position has not changed or there has been a shift in the x-axis"



