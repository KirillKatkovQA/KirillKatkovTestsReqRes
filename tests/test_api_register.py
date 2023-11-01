from data import expected_responses
import pytest


class TestRegister:
    @pytest.mark.parametrize("email, password, expected_response", [("eve.holt@reqres.in", "pistol",
                                                                     expected_responses.successful_register_response[0]
                                                                     ),
                                                                    ("george.bluth@reqres.in", "gitgut",
                                                                     expected_responses.successful_register_response[1]
                                                                     )])
    def test_register_successful(self, reqres_api, email, password, expected_response):
        result, status_code = reqres_api.post_register(email, password)
        reqres_api.assert_correct_response(result, status_code, expected_response)

    def test_register_unsuccessful(self, reqres_api):
        result, status_code = reqres_api.post_register("eve.holt@reqres.in", "")
        reqres_api.assert_register_unsuccessful(result, status_code, expected_responses.unsuccessful_register_response)
