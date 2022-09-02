
class Search():
    def __init__(self, driver):
        self.driver=driver
        self.search_name='q'

    def click_search(self):
        self.driver.find_element_by_name(self.search_name).clear()
