# coding: utf-8

"""
    Devbook

    Devbook API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import e2b.api.client
from e2b.api.client.models.environment_state_update import (
    EnvironmentStateUpdate,
)  # noqa: E501
from e2b.api.client.rest import ApiException


class TestEnvironmentStateUpdate(unittest.TestCase):
    """EnvironmentStateUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EnvironmentStateUpdate
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EnvironmentStateUpdate`
        """
        model = e2b.api.client.models.environment_state_update.EnvironmentStateUpdate()  # noqa: E501
        if include_optional :
            return EnvironmentStateUpdate(
                state = 'Building'
            )
        else :
            return EnvironmentStateUpdate(
                state = 'Building',
        )
        """

    def testEnvironmentStateUpdate(self):
        """Test EnvironmentStateUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()