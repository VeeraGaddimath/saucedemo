from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.ID, "inventory_container")

    def is_loaded(self):
        return self.driver.find_element(*self.inventory_container).is_displayed()
