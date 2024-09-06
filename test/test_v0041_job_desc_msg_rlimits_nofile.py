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

from slurm_rest.models.v0041_job_desc_msg_rlimits_nofile import V0041JobDescMsgRlimitsNofile

class TestV0041JobDescMsgRlimitsNofile(unittest.TestCase):
    """V0041JobDescMsgRlimitsNofile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041JobDescMsgRlimitsNofile:
        """Test V0041JobDescMsgRlimitsNofile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041JobDescMsgRlimitsNofile`
        """
        model = V0041JobDescMsgRlimitsNofile()
        if include_optional:
            return V0041JobDescMsgRlimitsNofile(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041JobDescMsgRlimitsNofile(
        )
        """

    def testV0041JobDescMsgRlimitsNofile(self):
        """Test V0041JobDescMsgRlimitsNofile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()