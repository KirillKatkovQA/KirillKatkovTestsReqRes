import json
from playwright.sync_api import Playwright


class ApiReqRes:
    def __init__(self, playwright: Playwright, base_url="https://reqres.in/api/", headless=True):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = playwright.request.new_context()
        self.base_url = base_url

    def close(self):
        self.context.dispose()
        self.browser.close()

    def get_list_users(self, page):
        response = self.context.get(
            url=self.base_url + f"users?page={page}"
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    def get_list_users_for_match(self, page):
        response = self.context.get(
            url=self.base_url + f"users?page={page}"
        )
        result_body = response.body()
        result_status_code = response.status
        return result_body, result_status_code

    def get_list_users_delay(self, delay):
        response = self.context.get(
            url=self.base_url + f"users?delay={delay}"
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    def get_single_user(self, user_id):
        response = self.context.get(
            url=self.base_url + f"users/{user_id}"
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    def post_user(self, name, job):
        response = self.context.post(
            url=self.base_url + "users",
            data={
                "name": f"{name}",
                "job": f"{job}"
            },
            headers={
                "Content-Type": "application/json"
            }
        )
        result_body = json.loads(response.body())
        user_id = result_body["id"]
        result_status_code = response.status
        return result_body, user_id, result_status_code

    def patch_user(self, user_id, name, job):
        response = self.context.post(
            url=self.base_url + f"users/{user_id}",
            data={
                "name": f"{name}",
                "job": f"{job}"
            },
            headers={
                "Content-Type": "application/json"
            }
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    def delete_user(self, user_id):
        response = self.context.delete(
            url=self.base_url + f"users/{user_id}"
        )
        result_status_code = response.status
        return result_status_code

    def get_resourse_list(self, page, per_page):
        response = self.context.get(
            url=self.base_url + f"unknown?page={page}&per_page={per_page}"
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    def get_single_resourse(self, resourse_id):
        response = self.context.get(
            url=self.base_url + f"unknown/{resourse_id}"
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    def post_register(self, email, password):
        response = self.context.post(
            url=self.base_url + f"register",
            data={
                "email": f"{email}",
                "password": f"{password}"
            },
            headers={
                "Content-Type": "application/json"
            }
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    def post_login(self, email, password):
        response = self.context.post(
            url=self.base_url + f"login",
            data={
                "email": f"{email}",
                "password": f"{password}"
            },
            headers={
                "Content-Type": "application/json"
            }
        )
        result_body = json.loads(response.body())
        result_status_code = response.status
        return result_body, result_status_code

    @staticmethod
    def assert_correct_response(result, result_status_code, expected_response):
        assert result == expected_response
        assert result_status_code == 200

    @staticmethod
    def assert_not_found(result, result_status_code, expected_response):
        assert result == expected_response
        assert result_status_code == 404

    @staticmethod
    def assert_user_created(result, user_id, result_status_code, name, job):
        assert result['name'] == name
        assert result['job'] == job
        assert result_status_code == 201
        assert user_id != 0

    @staticmethod
    def assert_user_updated(result, result_status_code, name, job):
        assert result['name'] == name
        assert result['job'] == job
        assert result_status_code == 201  # в описании API код ответа указан 200,
        # но по логике обновления должен быть (и в ответе приходит правильный) код 201

    @staticmethod
    def assert_user_deleted(status_code):
        assert status_code == 204

    @staticmethod
    def assert_register_unsuccessful(result, result_status_code, expected_response):
        assert result == expected_response
        assert result_status_code == 400

    @staticmethod
    def assert_login_unsuccessful(result, result_status_code, expected_response):
        assert result == expected_response
        assert result_status_code == 400
