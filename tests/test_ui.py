import pytest
from data.ui_test_parametrize import endpoints_data


class TestMainPage:
    def test_mainpage_available(self, reqres_ui):
        reqres_ui.goto("/")
        reqres_ui.assert_mainpage_load()

    def test_support_button_redirect(self, reqres_ui):
        reqres_ui.goto("/")
        reqres_ui.button_click("a[href='#support-heading']")
        reqres_ui.assert_url("https://reqres.in/#support-heading")

    def test_support_onetime_redirect(self, reqres_ui):
        reqres_ui.goto("/")
        reqres_ui.radio_choose("//input[@id='supportOneTime']")
        reqres_ui.button_click("//button[contains(text(),'Support ReqRes')]")
        reqres_ui.field_fill("15")
        reqres_ui.assert_onetime_support("15")

    def test_support_monthly(self, reqres_ui):
        reqres_ui.goto("/")
        reqres_ui.radio_choose("//input[@id='supportRecurring']")
        reqres_ui.button_click("//button[contains(text(),'Support ReqRes')]")
        reqres_ui.assert_monthly_support()

    def test_mainpage_to_swagger(self, reqres_ui):
        reqres_ui.goto("/")
        reqres_ui.button_click("//img[@alt='Swagger logo']")
        reqres_ui.assert_swagger_page()

    def test_upgrade_subscribe(self, reqres_ui):
        reqres_ui.goto("/")
        reqres_ui.button_click("//button[@id='trigger-pro']")
        reqres_ui.assert_subscribe_button()

    @pytest.mark.parametrize("key, request_url, status_code", endpoints_data)
    @pytest.mark.flaky(reruns=2, rerun_delay=5, min_passes=1)
    def test_request_endpoints_try(self, reqres_ui, key, request_url, status_code):
        reqres_ui.goto("/")
        reqres_ui.choose_endpoint(key)
        reqres_ui.assert_endpoint_choose(request_url, status_code)


@pytest.mark.flaky(reruns=2, rerun_delay=5, min_passes=1)
class TestAPIandUIResponsesMatches:
    def test_list_users_responses_matches(self, reqres_api, reqres_ui):
        reqres_ui.goto("/")
        reqres_ui.choose_endpoint("//li[@data-id='users']")
        ui_body, ui_status = reqres_ui.try_example("/api/users?page=2")
        print(ui_body, ui_status)
        api_body, api_status = reqres_api.get_list_users_for_match(2)
        print(api_body, api_status)
        reqres_ui.assert_responses_matches(ui_body, ui_status, api_body, api_status)
