class LogMenu():
    def __init__(self, driver):
        self.driver=driver
        self.menu_id='userNavigationLabel'

    def click_menu(self):
        self.driver.find_element_by_id(self.menu_id).click()
