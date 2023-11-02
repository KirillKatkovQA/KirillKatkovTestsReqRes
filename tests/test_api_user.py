from data import expected_responses
import pytest


class TestUsers:
    @pytest.mark.parametrize("page, expected_response", [(1, expected_responses.list_users_response[0]),
                                                         (2, expected_responses.list_users_response[1])])
    def test_list_users_correct_response(self, reqres_api, page, expected_response):
        result, status_code = reqres_api.get_list_users(page)
        reqres_api.assert_correct_response(result, status_code, expected_response)

    @pytest.mark.parametrize("user_id, expected_response", [(1, expected_responses.single_user_response[0]),
                                                            (2, expected_responses.single_user_response[1])])
    def test_single_user_found(self, reqres_api, user_id, expected_response):
        result, status_code = reqres_api.get_single_user(user_id)
        reqres_api.assert_correct_response(result, status_code, expected_response)

    @pytest.mark.parametrize("user_id", [23, 0, 99])
    def test_single_user_not_found(self, reqres_api, user_id):
        result, status_code = reqres_api.get_single_user(user_id)
        reqres_api.assert_not_found(result, status_code, expected_response={})

    @pytest.mark.flaky(reruns=2, rerun_delay=5, min_passes=1)
    @pytest.mark.parametrize("name, job", [("morpheus", "leader"), ("neo", "the chosen one"), ("smith", "agent")])
    def test_user_create(self, reqres_api, name, job):
        result, user_id_temp, status_code = reqres_api.post_user(name, job)
        reqres_api.assert_user_created(result, user_id_temp, status_code, name, job)
        return user_id_temp

    @pytest.mark.flaky(reruns=2, rerun_delay=5, min_passes=1)
    @pytest.mark.parametrize("name, job", [("morpheus", "leader"), ("neo", "the chosen one"), ("smith", "agent")])
    def test_user_update(self, reqres_api, name, job):
        user_id_temp = self.test_user_create(reqres_api, name, job)
        result, status_code = reqres_api.patch_user(user_id_temp, name, "zion resident")
        reqres_api.assert_user_updated(result, status_code, name, "zion resident")

    @pytest.mark.flaky(reruns=2, rerun_delay=5, min_passes=1)
    @pytest.mark.parametrize("name, job", [("morpheus", "leader"), ("neo", "the chosen one"), ("smith", "agent")])
    def test_user_delete(self, reqres_api, name, job):
        user_id_temp = self.test_user_create(reqres_api, name, job)
        status_code = reqres_api.delete_user(user_id_temp)
        reqres_api.assert_user_deleted(status_code)
        self.test_single_user_not_found(reqres_api, user_id=user_id_temp)

    def test_users_list_with_delay(self, reqres_api):
        result, status_code = reqres_api.get_list_users_delay(3)
        reqres_api.assert_correct_response(result, status_code, expected_responses.list_users_response_delay)
