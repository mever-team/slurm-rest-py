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

from slurm_rest.models.v0040_stats_msg_rpcs_by_type_inner import V0040StatsMsgRpcsByTypeInner

class TestV0040StatsMsgRpcsByTypeInner(unittest.TestCase):
    """V0040StatsMsgRpcsByTypeInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040StatsMsgRpcsByTypeInner:
        """Test V0040StatsMsgRpcsByTypeInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040StatsMsgRpcsByTypeInner`
        """
        model = V0040StatsMsgRpcsByTypeInner()
        if include_optional:
            return V0040StatsMsgRpcsByTypeInner(
                message_type = '',
                type_id = 56,
                count = 56,
                average_time = 56,
                total_time = 56
            )
        else:
            return V0040StatsMsgRpcsByTypeInner(
        )
        """

    def testV0040StatsMsgRpcsByTypeInner(self):
        """Test V0040StatsMsgRpcsByTypeInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
