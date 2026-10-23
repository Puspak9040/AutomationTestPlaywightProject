import pytest
from playwright.sync_api import Page
class ProductPage:
    def __init__(self, page: Page):
        self.page=page
        self.add_qty=page.locator('input[name="quantity"]')
        self.add_cart=page.locator("button#button-cart")
        self.cnf_msg=page.locator("div.alert.alert-success.alert-dismissible")
        self.cart_btn=page.locator('#cart')
        self.view_cart=page.locator('strong:has-text("View Cart")')

#set quantity
    def set_quantity(self,quantity):
        self.add_qty.fill("")
        self.add_qty.fill(quantity)
#add to cart button
    def add_to_cart(self):
        self.add_cart.click()

#get confirmation msg
    def get_conf_msg(self):
        return self.cnf_msg

#click cart item
    def click_cart_item(self):
        self.cart_btn.click()

#click view cart to see the shoping cart page
    def click_view_cart(self):
        self.view_cart.click()


