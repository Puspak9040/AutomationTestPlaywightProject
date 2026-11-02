import pytest
from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import Myaccount
from utilities.data_reader_util import read_json_data,read_csv_data,read_excel_data

#json_data=read_json_data("testdata\logindata.json")
#excel_data=read_excel_data("testdata\logindata.xlsx")
csv_data=read_csv_data("testdata\logindata.csv")
@pytest.mark.datadriven
@pytest.mark.parametrize("testName,email,password,expected",csv_data)
def test_login_data_driven(page,testName,email,password,expected):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account = Myaccount(page)

    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email_id(email)
    login_page.set_password(password)
    login_page.click_login()
    page.wait_for_timeout(5000)
    if expected=="success":
        expect(login_page.login_success()).to_be_visible(timeout=5000)

    elif expected=="failure":
        expect(login_page.txt_error_message
               ).to_contain_text("Warning: No match for E-Mail Address and/or Password.")
    page.wait_for_timeout(5000)
