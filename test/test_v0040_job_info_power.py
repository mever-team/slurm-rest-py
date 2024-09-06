# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.2&openapi/slurmdbd&openapi/v0.0.39&openapi/dbv0.0.39&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from slurm_rest.models.v0040_job_info_power import V0040JobInfoPower

class TestV0040JobInfoPower(unittest.TestCase):
    """V0040JobInfoPower unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040JobInfoPower:
        """Test V0040JobInfoPower
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040JobInfoPower`
        """
        model = V0040JobInfoPower()
        if include_optional:
            return V0040JobInfoPower(
                flags = [
                    null
                    ]
            )
        else:
            return V0040JobInfoPower(
        )
        """

    def testV0040JobInfoPower(self):
        """Test V0040JobInfoPower"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()