from selenium.webdriver.common.by import By



class SignUp:
    txt_info_xpath="//b[normalize-space()='Enter Account Information']"

    def __init__(self,driver):
        self.driver=driver

    def validateInfo(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_info_xpath).is_displayed()
        except:
            None




