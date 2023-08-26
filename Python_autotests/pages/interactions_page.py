import random
import time

from Python_autotests.locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, \
    ResizablePageLocators, DroppablePageLocators
from Python_autotests.pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_item(self, elements):
        item_list = self.element_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_item(self.locators.TAB_ITEM)
        item_list = random.sample(self.element_are_visible(self.locators.TAB_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.TAB_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID_LIST).click()
        order_before = self.get_sortable_item(self.locators.GRID_ITEM)
        item_list = random.sample(self.element_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.element_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.TAB_ITEM)
        active_element = self.element_is_visible(self.locators.TAB_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_LIST).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_and_height(self, value_of_size):
        width = value_of_size.split(";")[0].split(":")[1].replace(' ', '')
        height = value_of_size.split(";")[1].split(":")[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_and_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_and_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_and_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_and_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.TAB_SIMPLE).click()
        drag_div = self.element_is_visible(self.locators.DRAG_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_acceptable(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_ACCEPTABLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_not_acceptable(self):
        self.element_is_visible(self.locators.TAB_ACCEPT).click()
        drag_div = self.element_is_visible(self.locators.DRAG_NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_ACCEPTABLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_prevent_propogation_not_greedy(self):
        self.element_is_visible(self.locators.TAB_PREVENT_PROPOGATION).click()
        drag_div = self.element_is_visible(self.locators.DRAG_PREVENT)
        drop_div_outer = self.element_is_visible(self.locators.DROP_OUTER_NOT_GREEDY)
        drop_div_inner = self.element_is_visible(self.locators.DROP_INNER_NOT_GREEDY)
        self.action_drag_and_drop_to_element(drag_div, drop_div_inner)
        return drop_div_outer.text, drop_div_inner.text

    def drop_prevent_propogation_greedy(self):
        self.element_is_visible(self.locators.TAB_PREVENT_PROPOGATION).click()
        drag_div = self.element_is_visible(self.locators.DRAG_PREVENT)
        drop_div_outer = self.element_is_visible(self.locators.DROP_OUTER_GREEDY)
        drop_div_inner = self.element_is_visible(self.locators.DROP_INNER_GREEDY)
        self.action_drag_and_drop_to_element(drag_div, drop_div_inner)
        return drop_div_outer.text, drop_div_inner.text

    def drop_will_revert_draggable(self):
        self.element_is_visible(self.locators.TAB_REVERT_DRAGGABLE).click()
        will_revert = self.element_is_visible(self.locators.DRAG_WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_REVERT)
        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_drag = will_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_drag, position_after_revert

    def drop_revert_draggable(self, type_drag):
        drags = {
            'will_revert':
                {'revert': self.locators.DRAG_WILL_REVERT, },
            'not_revert':
                {'revert': self.locators.DRAG_NOT_REVERT, },
        }
        self.element_is_visible(self.locators.TAB_REVERT_DRAGGABLE).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_drag = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_drag, position_after_revert
