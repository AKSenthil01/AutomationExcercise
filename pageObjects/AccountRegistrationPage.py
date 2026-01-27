from selenium.webdriver.common.by import By
class AccountRegistrationPage:
    lnk_user_xpath="//input[@placeholder='Name']"
    lnk_email_xpath="//input[@data-qa='signup-email']"
    lnk_signup_xpath="//button[normalize-space()='Signup']"
    lnk_ad_xpath="//div[@class='grippy-host']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnAd(self):
        self.driver.find_element(By.XPATH,self.lnk_ad_xpath).click()

    def setName(self,name):
        self.driver.find_element(By.XPATH,self.lnk_user_xpath).send_keys(name)

    def setEmail(self,pwd):
        self.driver.find_element(By.XPATH,self.lnk_email_xpath).send_keys(pwd)

    def clickSignup(self):
        self.driver.find_element(By.XPATH,self.lnk_signup_xpath).click()







