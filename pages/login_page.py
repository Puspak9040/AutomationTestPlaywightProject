from playwright.sync_api import Page,expect
class LoginPage:
    def __init__(self,page:Page):
    #locatior
      self.txt_email_id=page.locator('input[name="email"]')
      self.txt_password=page.locator('input[name="password"]')
      self.button_login=page.locator('input.btn.btn-primary')
      self.txt_error_message = page.locator("div.alert.alert-danger")
      self.myaccount_heading=page.locator('div[id="content"] h2:has-text("My Account")')
    #action method
    def set_email_id(self,email):
        self.txt_email_id.fill(email)

    def set_password(self,password):
        self.txt_password.fill(password)

    def click_login(self):
        self.button_login.click()

    def get_login_erorr_message(self,message):
        return self.txt_error_message
    def login_success(self):
        return self.myaccount_heading