from testpage import OperationHelper
import time

import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)
    name = data["username"]
    password = data["password"]


def test_step1(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("testlog")
    testpage.enter_pass("testpass")
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_error_text() == "401", "test_step1 FAIL"


def test_step2(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(password)
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_profile_text() == f"Hello, {name}", "test_step2 FAIL"


def test_step3(browser):
    testpage = OperationHelper(browser)
    testpage.click_to_do_new_post()
    testpage.enter_title("Hello")
    testpage.enter_description("error")
    testpage.enter_content("Good luck")
    testpage.click_save_post_button()
    time.sleep(5)
    assert testpage.get_title_text() == "Hello", "test_step3 FAIL"