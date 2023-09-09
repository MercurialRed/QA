from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    GRID_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    TAB_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')
    GRID_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle '
                                             'react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[class="resizable-nolimit mt-4"] span[class="react-resizable-handle '
                                         'react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')


class DroppablePageLocators:
    # Simple
    TAB_SIMPLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_SIMPLE = (By.CSS_SELECTOR, 'div[id="droppableExample-tabpane-simple"] div[id="droppable"]')

    # Accept
    TAB_ACCEPT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    DRAG_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    DRAG_NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="droppable"]')

    # Prevent Propogation
    TAB_PREVENT_PROPOGATION = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    DRAG_PREVENT = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    DROP_OUTER_NOT_GREEDY = (By.CSS_SELECTOR, 'div[id="ppDropContainer"] div[id="notGreedyDropBox"] p:nth-child(1)')
    DROP_INNER_NOT_GREEDY = (By.CSS_SELECTOR, 'div[id="ppDropContainer"] div[id="notGreedyInnerDropBox"]')
    DROP_OUTER_GREEDY = (By.CSS_SELECTOR, 'div[id="ppDropContainer"] div[id="greedyDropBox"] p:nth-child(1)')
    DROP_INNER_GREEDY = (By.CSS_SELECTOR, 'div[id="ppDropContainer"] div[id="greedyDropBoxInner"]')

    # Revert Draggable
    TAB_REVERT_DRAGGABLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    DRAG_WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    DRAG_NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_REVERT = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"]')


class DraggablePageLocators:
    # Simple
    TAB_SIMPLE = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_SIMPLE = (By.CSS_SELECTOR, 'div[id="dragBox"]')

    # Axis Restricted
    TAB_AXIS_RESTRICTED = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    DRAG_RESTRICTED_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    DRAG_RESTRICTED_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

