from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from pageObjects.SignUpPage import SignUp





class Test001AccountReg:
    baseURL="https://automationexercise.com/"

    def test_AccountReg(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.HP=HomePage(self.driver)
        self.HP.clickLogin()
        self.driver.implicitly_wait(10)
        self.AccReg=AccountRegistrationPage(self.driver)
        self.driver.implicitly_wait(10)
        #self.AccReg.clickOnAd()
        self.AccReg.setName("SenthilKumar")
        self.AccReg.setEmail("sen1977@gmail.com")
        self.AccReg.clickSignup()
        self.driver.implicitly_wait(10)
        self.sinfo=SignUp(self.driver)
        self.msg=self.sinfo.validateInfo()
        print(self.msg)
        if self.msg:
            assert True
        else:
            assert False

