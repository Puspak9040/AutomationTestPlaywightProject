import pytest
from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RandomDataUtil

def test_user_registration(page):
    home_page=HomePage(page)
    registration_page=RegistrationPage(page)
    home_page.click_my_account()
    page.wait_for_timeout(5000)
    home_page.click_register()

    random_data=RandomDataUtil()
    first_name=random_data.get_first_name()
    last_name=random_data.get_last_name()
    email=random_data.get_email()
    password=random_data.get_password()
    phone=random_data.get_phone()

    register_page=RegistrationPage(page)
    register_page.set_firstname(first_name)
    register_page.set_lastname(last_name)
    register_page.set_email(email)
    register_page.set_password(password)
    register_page.set_confirm_password(password)
    register_page.set_phone(phone)

    register_page.privacy_policy()
    register_page.click_button_continue()
    #assertion
    confirm_msg=register_page.conf_msg_registation()
    expect(confirm_msg).to_have_text("Your Account Has Been Created!")
