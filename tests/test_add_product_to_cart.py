import pytest
from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage
from config import Config
def test_add_product_to_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    search_page = SearchResultsPage(page)
    config = Config()
#search product
    home_page.enter_product_name(config.product_name)
    home_page.click_search_button()
#assert search header
    expect(search_page.get_search_page_header()).to_be_visible(timeout=5000)
#assert existing product visible
    expect(search_page.is_product_exist(config.product_name)).to_be_visible()
#select product
    search_page.select_product(config.product_name)
#set product quantity
    product_page.set_quantity(config.product_quantity)
#add product to cart
    product_page.add_to_cart()
#assert product add to cart
    product_add_msg=product_page.get_conf_msg()
    expect(product_add_msg).to_be_visible()
#click to cart item
    product_page.click_cart_item()
#click to see product which is added to cart
    product_page.click_view_cart()
