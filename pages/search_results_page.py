import pytest
from playwright.sync_api import Page
from pages.product_page import ProductPage
class SearchResultsPage:
    def __init__(self,page:Page):
        self.page = page
        self.search_page_header=page.locator('#content h1:has-text("Search ")')
        self.search_product=page.locator("h4> a")
#page header
    def get_search_page_header(self):
        return self.search_page_header
#product verification
    def is_product_exist(self,product_name):
        count=self.search_product.count()
        for i in range(count):
            product=self.search_product.nth(i)
            title=product.text_content()
            if title and title.strip()==product_name:
                return product
#product selection
    def select_product(self,product_name):
        count=self.search_product.count()
        for i in range(count):
            product=self.search_product.nth(i)
            title=product.text_content()
            if title and title.strip()==product_name:
                product.click()
                return ProductPage(self.page)

#count all the product
    def get_count_all_product(self,product_name):
        count=self.search_product.count()
        return count
