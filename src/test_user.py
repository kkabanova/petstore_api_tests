import json

from assertpy import assert_that

from data_preparation.data_preparation import (
    DataPreparation,
)


class TestUser:
    def test_create_user(self):
        response, payload = DataPreparation().create_user()
        actual_status_code = response.status_code
        actual_response_json = response.json()
        expected_response_json = {
            "code": 200,
            "type": "unknown",
            "message": str(json.loads(payload).get("id")),
        }

        assert_that(actual_status_code).is_equal_to(200)
        assert_that(actual_response_json).is_equal_to(expected_response_json)
