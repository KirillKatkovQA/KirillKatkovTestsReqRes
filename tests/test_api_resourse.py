from data import expected_responses
import pytest


class TestResourses:
    @pytest.mark.parametrize("page, per_page, expected_response", [(1, 6, expected_responses.resource_list_response[0]),
                                                                   (2, 3, expected_responses.resource_list_response[1]),
                                                                   (3, 1, expected_responses.resource_list_response[2])
                                                                   ])
    def test_list_resourse_correct_response(self, reqres_api, page, per_page, expected_response):
        result, status_code = reqres_api.get_resourse_list(page, per_page)
        reqres_api.assert_correct_response(result, status_code, expected_response)

    @pytest.mark.parametrize("resouse_id, expected_response", [(2, expected_responses.single_resourse_response[0]),
                                                               (4, expected_responses.single_resourse_response[1])
                                                               ])
    def test_single_resourse_found(self, reqres_api, resouse_id, expected_response):
        result, status_code = reqres_api.get_single_resourse(resouse_id)
        print(result, status_code)
        reqres_api.assert_correct_response(result, status_code, expected_response)

    @pytest.mark.parametrize("resouse_id", (23, 0, 99))
    def test_single_resourse_not_found(self, reqres_api, resouse_id):
        result, status_code = reqres_api.get_single_resourse(resouse_id)
        print(result, status_code)
        reqres_api.assert_not_found(result, status_code, expected_response={})
