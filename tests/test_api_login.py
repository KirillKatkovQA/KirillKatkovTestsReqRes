from data import expected_responses


class TestLogin:
    def test_login_successful(self, reqres_api):
        result, status_code = reqres_api.post_login("eve.holt@reqres.in", "cityslicka")
        reqres_api.assert_correct_response(result, status_code, expected_responses.successful_login_response)

    def test_login_unsuccessful(self, reqres_api):
        result, status_code = reqres_api.post_login("eve.holt@reqres.in", "")
        reqres_api.assert_login_unsuccessful(result, status_code, expected_responses.unsuccessful_login_response)
