class ProfilePage():
    def __init__(self, driver):
        self.driver=driver
        self.profile_text='Anvesh'

    def click_profile(self):
        self.driver.find_element_by_link_text(self.profile_text).click()
