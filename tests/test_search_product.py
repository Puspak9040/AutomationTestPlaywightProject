import pytest
from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from config import Config
from pages.search_results_page import SearchResultsPage
def test_search_products_page(page):
    home_page = HomePage(page)
    search_page = SearchResultsPage(page)
    config=Config()
    home_page.enter_product_name(config.product_name)
    home_page.click_search_button()

    expect(search_page.get_search_page_header()).to_be_visible(timeout=5000)
    expect(search_page.is_product_exist(config.product_name)).to_be_visible(timeout=5000)
