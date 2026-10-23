import pytest
from playwright.sync_api import Page,expect

import config
from pages.home_page import HomePage
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.my_account_page import Myaccount
from config import Config

def test_user_logout(page):
    home_page=HomePage(page)
    login_page=LoginPage(page)
    logout_page=LogoutPage(page)
    my_account=Myaccount(page)
    config=Config()

    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email_id(config.email)
    login_page.set_password(config.password)
    login_page.click_login()

    expect(login_page.login_success()).to_be_visible()

    #click logout from myaccount dropdown
    my_account.click_my_account_dropdown()
    my_account.click_logout()
    heading_logout=logout_page.visible_account_logout()
    expect(heading_logout).to_be_visible()
    logout_page.get_continue_btn()
    #expect(page.url).to_have_url("https://tutorialsninja.com/demo/index.php?route=common/home")
    page.wait_for_timeout(5000)

