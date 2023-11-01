from playwright.sync_api import Playwright, expect


class UiReqRes:
    def __init__(self, playwright: Playwright, base_url="https://reqres.in", headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def button_click(self, button_locator):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator(button_locator).click()

    def radio_choose(self, radio_locator):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator(radio_locator).click()

    def field_fill(self, value):
        self.page.get_by_placeholder("$10").fill(value)
        self.page.wait_for_timeout(2000)

    def choose_endpoint(self, endpoint_locator):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.locator(endpoint_locator).click()

    def try_example(self, example_locator):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)
        with self.page.expect_navigation() as navigation_info:
            self.page.get_by_text(example_locator).click()
        response = navigation_info.value
        body = response.body()
        status = response.status
        return body, status

    def assert_mainpage_load(self):
        expect(self.page.get_by_text("Test your front-end against a real API")).to_be_visible()

    def assert_url(self, expected_url):
        self.page.wait_for_timeout(2000)
        assert self.page.url == expected_url

    def assert_onetime_support(self, value):
        self.page.wait_for_load_state("load")
        expect(self.page.get_by_text("Support ReqRes")).to_be_visible()
        expect(self.page.get_by_test_id("product-summary-total-amount")).to_contain_text(value)

    def assert_monthly_support(self):
        self.page.wait_for_load_state("load")
        expect(self.page.get_by_text("Подписаться на Support ReqRes")).to_be_visible()

    def assert_swagger_page(self):
        self.page.wait_for_load_state("load")
        expect(self.page.get_by_text("ReqRes API")).to_be_visible()

    def assert_subscribe_button(self):
        self.page.wait_for_load_state("load")
        expect(self.page.locator("//input[@id='mc-embedded-subscribe']")).to_be_visible()

    def assert_endpoint_choose(self, request_url, status_code):
        self.page.wait_for_timeout(1000)
        expect(self.page.locator("//span[@class='url']")).to_contain_text(request_url)
        response_code = self.page.locator("//span[@data-key='response-code']").text_content()
        assert expect(self.page.locator("//span[@data-key='response-code']"))
        assert status_code == response_code

    @staticmethod
    def assert_responses_matches(ui_body, ui_status, api_body, api_status):
        assert ui_body == api_body
        assert ui_status == api_status
