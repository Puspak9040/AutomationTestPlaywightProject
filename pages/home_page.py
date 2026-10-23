from playwright.sync_api import Page,expect
class HomePage:
    def __init__(self,page:Page):
        self.page = page
#locators
        self.link_my_account=page.locator('span:has-text("My Account")')
        self.link_register=page.locator('a:has-text("Register")')
        self.link_login=page.locator('a:has-text("Login")')
        self.search_box=page.locator('input[name="search"]')
        self.search_button=page.locator('#search button[type="button"]')

#actions
    #return tittle of the page
    def get_home_page_tittle(self):
        tittle=self.page.title()
        return tittle
    #click on myaccount
    def click_my_account(self):
        self.link_my_account.click()
    # click register
    def click_register(self):
        self.link_register.click()
    #click login
    def click_login(self):
        self.link_login.click()
    #enter product name into search box
    def enter_product_name(self,product_name:str):
        self.search_box.fill(product_name)
    #click  search button
    def click_search_button(self):
        self.search_button.click()
