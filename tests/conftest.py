import pytest
from playwright.sync_api import sync_playwright
from page_objects.application_api import ApiReqRes
from page_objects.application_ui import UiReqRes


@pytest.fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope='class')
def reqres_api(get_playwright):
    reqres_new = ApiReqRes(get_playwright, base_url="https://reqres.in/api/")
    yield reqres_new
    reqres_new.close()


@pytest.fixture(scope='class')
def reqres_ui(get_playwright):
    reqres_new = UiReqRes(get_playwright, base_url="https://reqres.in")
    yield reqres_new
    reqres_new.close()
