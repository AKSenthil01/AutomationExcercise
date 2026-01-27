from selenium.webdriver.common.by import By

class HomePage():
    lnk_login_xpath="//a[normalize-space()='Signup / Login']"

    def __init__(self,driver):
        self.driver=driver


    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.lnk_login_xpath).click()
