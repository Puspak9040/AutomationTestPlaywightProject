from playwright.sync_api import Page
class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_continue=page.locator('.btn.btn-primary')
        self.account_logout_headding=page.locator('#content h1:has-text("Account Logout")')

    def click_ccontinue(self):
        self.btn_continue.click()


    def get_continue_btn(self):
        return self.btn_continue.click()

    def visible_account_logout(self):
        return self.account_logout_headding