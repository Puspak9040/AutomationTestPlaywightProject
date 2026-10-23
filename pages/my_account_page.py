from playwright.sync_api import Page

class Myaccount:
    def __init__(self,page:Page):
        self.page=Page

        self.msg_heading=page.locator('#content h2:has-text("My Account")')
        self.link_logout=page.locator("li[class='dropdown open'] li:nth-child(5) a:nth-child(1)")
        self.my_account_dropdown=page.locator(".caret")


       #action methodd
    def get_my_account_page_heading(self):
            return self.msg_heading

    def click_logout(self):
        self.link_logout.click()


    def get_page_title(self):
        return self.page.title()

    def click_my_account_dropdown(self):
        self.my_account_dropdown.click()