import pytest
from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import Config
def test_invalid_user_login(page):
    home_page= HomePage(page)
    login_page = LoginPage(page)
    config=Config()

    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email_id(config.invalid_email)
    login_page.set_password(config.invalid_password)
    login_page.click_login()
    expect(login_page.get_login_erorr_message()).to_be_visible()
    page.wait_for_timeout(500)
@pytest.mark.skip
def test_valid_user_login(page):
    home_page= HomePage(page)
    login_page = LoginPage(page)
    config = Config()
    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email_id(config.email)
    login_page.set_password(config.password)
    login_page.click_login()
    expect(login_page.login_success()).to_be_visible()
    page.wait_for_timeout(500)

