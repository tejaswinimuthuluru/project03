import time
from selenium import webdriver
import unittest
import sys
import os
from projects.facebook.pages.search import Search
from projects.facebook.pages.login_page import LoginPage
from projects.facebook.pages.profile import ProfilePage
from projects.facebook.pages.logout_menu import LogMenu
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__),"..",'..'))
class ClassName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.facebook.com/')
#login_page
    def test_login(self):
        login=LoginPage(self.driver)
        login.enter_username('rayankulaanvesh.kumar')
        login.enter_password('8801531511')
        login.click_login()
#profile_page
    def test_profiepage(self):
        time.sleep(10)
        profile=ProfilePage(self.driver)
        profile.click_profile()
# search
    def test_search(self):
        time.sleep(10)
        search=Search(self.driver)
        search.click_search()
#logout  menu
    def test_logmenu(self):
        time.sleep(20)
        lomenu=LogMenu(self.driver)
        lomenu.click_menu()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:/projects/facebook/Report'))
