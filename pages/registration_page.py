from playwright.sync_api import Page,expect
class RegistrationPage:
    def __init__(self,page:Page):
        self.page=page

    #locators
        #input fills
        self.txt_first_name=page.locator('#input-firstname')
        self.txt_last_name=page.locator('#input-lastname')
        self.txt_email=page.locator('#input-email')
        self.txt_phone=page.locator('#input-telephone')
        self.txt_password=page.locator('#input-password')
        self.txt_confirm_password=page.locator('#input-confirm')

        #checkbox radio buttons
        self.checkbox=page.locator('input[name="agree"]')
        self.button_continue=page.locator('input[value="Continue"]')
        #successfully login message
        self.msg_registation=page.locator('h1:has-text("Your Account Has Been Created!")')

    #Action method
    def set_firstname(self,fname):
        self.txt_first_name.fill(fname)

    def set_lastname(self,lname):
        self.txt_last_name.fill(lname)

    def set_email(self,email):
        self.txt_email.fill(email)

    def set_phone(self,phone):
        self.txt_phone.fill(phone)

    def set_password(self,password):
        self.txt_password.fill(password)

    def set_confirm_password(self,password):
        self.txt_confirm_password.fill(password)


    def privacy_policy(self):
        self.checkbox.check()

    def click_button_continue(self):
        self.button_continue.click()

    def conf_msg_registation(self):
        return self.msg_registation